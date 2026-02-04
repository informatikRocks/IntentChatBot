

import nltk
import numpy as np
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence: str) -> list[str]:
    """
    Tokenize a sentence into words.
    "Wie geht es dir?" -> ["Wie", "geht", "es", "dir", "?"]
    """
    return nltk.word_tokenize(sentence)




