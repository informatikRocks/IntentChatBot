

class IntentHandler:
    def __init__(self, nlp_engine: NLP_Engine):
        self.engine = nlp_engine

    def handle(self, text: str):
        """
        analysis_result ist das Dictionary, das engine.analyze() ausspuckt.
        Es enthält {'entities': [...], 'lemmas': [...]}
        """
        
