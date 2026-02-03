
import spacy
from spacy.pipeline import EntityRuler

class NLP_Engine:
    def __init__(self):
        self.nlp = spacy.load("de_core_news_sm")
        self.ruler=self.nlp.add_pipe("entity_ruler", before="ner")
        self._setup_patterns()


    def _setup_patterns(self):
        patterns = [



            # ... deine alten TECH patterns ...
            {"label": "TECH", "pattern": [{"LOWER": "react"}]},
            {"label": "TECH", "pattern": [{"LOWER": "python"}]},
            {"label": "TECH", "pattern": [{"LOWER": "typescript"}]},
            
            # Intents
            {"label": "INTENT_PROJEKTE", "pattern": [{"LEMMA": "projekt"}]},
            {"label": "INTENT_PROJEKTE", "pattern": [{"LOWER": "portfolio"}]},
            {"label": "INTENT_KONTAKT", "pattern": [{"LEMMA": "kontakt"}]},
            {"label": "INTENT_KONTAKT", "pattern": [{"LOWER": "email"}]},
            
            # NEU: Profile Intents (Name, Wer bist du?)
            {"label": "INTENT_PROFILE", "pattern": [{"LOWER": "name"}]},
            {"label": "INTENT_PROFILE", "pattern": [{"LOWER": "wer"}, {"LOWER": "bist"}]},

            # Skills Intent
        {"label": "INTENT_SKILLS", "pattern": [{"LEMMA": "skill"}]},
        {"label": "INTENT_SKILLS", "pattern": [{"LEMMA": "können"}]},
        {"label": "INTENT_SKILLS", "pattern": [{"LEMMA": "Fähigkeit"}]},
        
        # Hobbies Intent
        {"label": "INTENT_HOBBIES", "pattern": [{"LEMMA": "Hobby"}]},
        {"label": "INTENT_HOBBIES", "pattern": [{"LEMMA": "Freizeit"}]},
        {"label": "INTENT_HOBBIES", "pattern": [{"LOWER": "frei"}, {"LOWER": "zeit"}]}


        ]
        self.ruler.add_patterns(patterns)


    def analyze(self, text: str):
        doc = self.nlp(text)
        return {
            "text": text,
            "entities": [(ent.text, ent.label_) for ent in doc.ents],
            "lemmas": [(token.text, token.lemma_) for token in doc if not token.is_stop]
        }

engine = NLP_Engine()