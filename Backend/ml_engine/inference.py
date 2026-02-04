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