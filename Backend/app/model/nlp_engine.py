
import spacy
from spacy.pipeline import EntityRuler

class NLP_Engine:
    def __init__(self):
        self.nlp = spacy.load("de_core_news_sm")
        self.ruler=self.nlp.add_pipe("entity_ruler", before="ner")
        self._setup_patterns()


    def _setup_patterns(self):
        patterns = [{"label": "TECH", "pattern": [{"LOWER": "react"}]},
            {"label": "TECH", "pattern": [{"LOWER": "python"}]},
            {"label": "TECH", "pattern": [{"LOWER": "typescript"}]},
            {"label": "TECH", "pattern": [{"LOWER": "node.js"}]},
            
            # Intent-Erkennung (Was will der User?)
            {"label": "INTENT_PROJEKTE", "pattern": [{"LEMMA": "Projekt"}]},
            {"label": "INTENT_PROJEKTE", "pattern": [{"LOWER": "portfolio"}]},
            {"label": "INTENT_KONTAKT", "pattern": [{"LEMMA": "kontakt"}]},
            {"label": "INTENT_KONTAKT", "pattern": [{"LOWER": "email"}]}]


        self.ruler.add_patterns(patterns)

    def analyze(self, text: str):
        doc = self.nlp(text)
        return {
            "text": text,
            "entities": [(ent.text, ent.label_) for ent in doc.ents],
            "lemmas": [(token.text, token.lemma_) for token in doc if not token.is_stop]
        }

engine = NLP_Engine()