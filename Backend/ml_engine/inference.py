import torch
import random 
import json
import os
from model import NeuralNet
from nltk_utils import tokenize, bag_of_words


# Pfad Logik
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "data/saved_models/chat_model.pth")
INTENTS_PATH = os.path.join(BASE_DIR, "data/intents.json")


device = "cuda" if torch.cuda.is_available() else "cpu"

with open(INTENTS_PATH, "r", encoding="utf-8") as json_data:
    intents = json.load(json_data)

data = torch.load(MODEL_PATH)
model = NeuralNet(data["input_size"], data["hidden_size"], data["output_size"]).to(device)
model.load_state_dict(data["model_state"])
model.eval()


all_words = data["all_words"]
tags = data["tags"]

def get_intent_response(msg: str) -> str:
    """
    Get a response from the chatbot based on the input message.
    
    Args:
        msg (str): The input message from the user.
        
    Returns:
        str: The chatbot's response.
    """
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent["responses"])
    
    return "Entschuldigung, das habe ich nicht verstanden. Kannst du das anders formulieren?"