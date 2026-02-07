import torch
import random 
import json
import os
import sys

# Pfad-Magie
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from utils.nltk_utils import tokenize, bag_of_words
from intent.model import NeuralNet
from sentiment.model import SentimentModel

# --- PFADE ---
INTENT_MODEL_PATH = os.path.join(current_dir, "data/saved_models/chat_model.pth")
SENTIMENT_MODEL_PATH = os.path.join(current_dir, "data/saved_models/sentiment_model.pth")
INTENTS_PATH = os.path.join(current_dir, "data/intents.json")

device = "cuda" if torch.cuda.is_available() else "cpu"

# 1. INTENTS JSON LADEN
with open(INTENTS_PATH, "r", encoding="utf-8") as json_data:
    intents = json.load(json_data)

# 2. INTENT MODELL LADEN
intent_data = torch.load(INTENT_MODEL_PATH, map_location=device)

# Da deine save_model Funktion "input_layer" statt "input_size" benutzt hat:
input_layer = intent_data["input_layer"]
hidden_layer = intent_data["hidden_layer"]
output_layer = intent_data["output_layer"]
all_words = intent_data["all_words"]
tags = intent_data["tags"]

model_intent = NeuralNet(input_layer, hidden_layer, output_layer).to(device)
model_intent.load_state_dict(intent_data["model_state"])
model_intent.eval()

# 3. SENTIMENT MODELL LADEN
# Standard-Werte, falls Laden fehlschlägt
model_sentiment = None
all_words_sentiment = []
tags_sentiment = {0: "negative", 1: "neutral", 2: "positive"} # Fallback

try:
    if os.path.exists(SENTIMENT_MODEL_PATH):
        sentiment_data = torch.load(SENTIMENT_MODEL_PATH, map_location=device)
        
        input_layer_s = sentiment_data["input_layer"]
        hidden_layer_s = sentiment_data["hidden_layer"]
        output_layer_s = sentiment_data["output_layer"]
        all_words_sentiment = sentiment_data["all_words"]
        
        # Falls Tags mitgespeichert wurden, nehmen wir sie, sonst den Fallback
        if "tags" in sentiment_data:
            tags_sentiment = sentiment_data["tags"]
        
        model_sentiment = SentimentModel(input_layer_s, hidden_layer_s, output_layer_s).to(device)
        model_sentiment.load_state_dict(sentiment_data["model_state"])
        model_sentiment.eval()
        print("✅ Sentiment Modell geladen.")
    else:
        print(f"⚠️ Datei nicht gefunden: {SENTIMENT_MODEL_PATH}")

except Exception as e:
    print(f"❌ Fehler beim Laden des Sentiment-Modells: {e}")
    model_sentiment = None


def get_inference_response(msg: str):
    """
    Analysiert den Satz und gibt (Tag, Antwort, Stimmung) zurück.
    """
    # Tokenize nur EINMAL für beide Modelle
    sentence = tokenize(msg)
    
    # --- A. SENTIMENT ---
    sentiment_label = "neutral"

    if model_sentiment:
        X_sent = bag_of_words(sentence, all_words_sentiment)
        X_sent = X_sent.reshape(1, X_sent.shape[0])
        X_sent = torch.from_numpy(X_sent).to(device)
        
        output_sent = model_sentiment(X_sent)
        _, predicted_sentiment = torch.max(output_sent, dim=1)
        
        # Sicherer Zugriff auf das Label (falls Dictionary oder Liste)
        idx = predicted_sentiment.item()
        if isinstance(tags_sentiment, dict):
             sentiment_label = tags_sentiment.get(idx, "neutral")
        else:
             sentiment_label = tags_sentiment[idx]

    # --- B. INTENT ---
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    
    output = model_intent(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    response = "Tut mir leid, das habe ich nicht verstanden."

    # --- FIX FÜR DEINEN LOGIK-FEHLER ---
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent["responses"])
                break # WICHTIG: Suche beenden, sobald gefunden!
    else:
        # Nur wenn die Wahrscheinlichkeit zu niedrig ist, setzen wir es auf unknown
        tag = "unknown"

    return tag, response, sentiment_label