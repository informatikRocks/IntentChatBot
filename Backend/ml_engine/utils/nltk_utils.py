

import nltk
import numpy as np
from nltk.stem import PorterStemmer

# ----------
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# -----------

stemmer = PorterStemmer()

def tokenize(sentence: str) -> list[str]:
    """
    Tokenize a sentence into words.
    Example: "Wie geht es dir?" -> ["Wie", "geht", "es", "dir", "?"]
    """
    return nltk.word_tokenize(sentence)


def stem(word: str) -> str:
    """
    Stem a word to its root form.
    Example: "running" -> "run"
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence: list[str], all_words: list[str]) -> np.ndarray:
    """
    Create a bag-of-words representation of the tokenized sentence.
    Example:
    tokenized_sentence = ["hello", "how", "are", "you"]
    all_words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    -> [0, 1, 0, 1, 0, 0, 0]
    """
    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)

    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag




