import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import sys
import os

# --- PFAD-MAGIE ---
current_dir = os.path.dirname(os.path.abspath(__file__)) # .../sentiment
ml_engine_dir = os.path.dirname(current_dir)             # .../ml_engine
backend_dir = os.path.dirname(ml_engine_dir)             # .../Backend

# 1. Backend zum Pfad hinzufügen (für ml_engine Imports)
sys.path.append(backend_dir)
# 2. Den aktuellen Ordner AUCH hinzufügen (damit 'model.py' gefunden wird)
sys.path.append(current_dir)

# Importe
from ml_engine.utils.pytorch_helper import save_model
from ml_engine.utils.nltk_utils import tokenize, stem, bag_of_words

# Jetzt findet er 'model', weil wir 'current_dir' hinzugefügt haben
# ODER du nutzt den absoluten Import: from ml_engine.sentiment.model import SentimentModel
from model import SentimentModel 

# --- KORREKTUR 1: Daten liegen in ml_engine/data ---
file_path = os.path.join(ml_engine_dir, "data/sentiment.json")

# Prüfen ob Datei existiert
if not os.path.exists(file_path):
    print(f"FEHLER: Datei nicht gefunden unter: {file_path}")
    print("Bitte prüfe, ob die Datei 'sentiment.json' wirklich im Ordner 'ml_engine/data' liegt.")
    sys.exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    sentiments = json.load(f)

# --- AB HIER BLEIBT ALLES GLEICH ---
all_words = []
xy = []

for sentiment in sentiments:
    sentence = sentiment['text']
    label = sentiment['label']
    tokens = tokenize(sentence)
    all_words.extend(tokens)
    xy.append((tokens, label))

ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

X_train = []
y_train = []

for (pattern_sentence, label) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

class SentimentDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples
    
# Hyperparameters
batch_size = 8
hidden_size = 8
num_classes = 3 
input_size = len(X_train[0])
learning_rate = 0.001
num_epochs = 1000

dataset = SentimentDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = SentimentModel(input_size, hidden_size, num_classes).to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

print("Starte Sentiment Training...")
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device).float()
        labels = labels.to(dtype=torch.long).to(device)

        outputs = model(words)
        loss = loss_fn(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# --- KORREKTUR 2: Speichern in ml_engine/data/saved_models ---
save_path = os.path.join(ml_engine_dir, "data/saved_models")
os.makedirs(save_path, exist_ok=True)

sentiment_tags = ["negative", "neutral", "positive"]

save_model(modl=model,
           target_dir=save_path,
           model_name="sentiment_model.pth",
           input_size=input_size,
           hidden_size=hidden_size,
           output_size=num_classes,
           all_words=all_words,
           tags=sentiment_tags)
