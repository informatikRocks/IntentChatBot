
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ml_engine.utils.nltk_utils import tokenize, stem, bag_of_words

phrase = "Hallo Simon, was sind deine Hobbys?"
tokens = tokenize(phrase)
print(f"Tokens: {tokens}")

stems = [stem(w) for w in tokens]
print(f"Stems: {stems}")

# Ein fiktives Vokabular zum Testen von Bag of Words
vokabular = ["hallo", "simon", "projekt", "hobbi", "code"]
bog = bag_of_words(tokens, vokabular)
print(f"Bag of Words: {bog}")