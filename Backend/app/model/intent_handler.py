
from .data_manager import DataManager


class IntentHandler:
    def __init__(self):
        self.data_manager = DataManager()

    def handle_intent(self, nlp_analysis):
        """Decides based on the NLP analysis what the user wants"""
        entities = nlp_analysis.get("entities", [])
        
        detected_intents = [label for text, label in entities]
        tech_filter = next((text for text, label in entities if label == "TECH"), None)

        if "INTENT_KONTAKT" in detected_intents:
            return self._handle_contact()
        
        if "INTENT_PROJEKTE" in detected_intents:
            return self._handle_projects(tech_filter)
        
        return "Ich verstehe nicht ganz. Kannst du das anders formulieren?"


    def _handle_projects(self, tech_filter):
        """Helpermethods for handling projects"""
        projects = self.data_manager.get_projects(tech_filter)
        if not projects:
            return "Ich habe keine Projekte, die zu deiner Anfrage passen."
        
        response = "Hier sind einige meiner Projekte:"
        if tech_filter:
            response = f"Hier sind einige meiner {tech_filter} Projekte:"

        for p in projects:
            stack_str = ", ".join(p.get("tech_stack", []))
            response += f"\n- {p['name']}: {p['description']} (Stack: {stack_str})"

        return response
    

    def _handle_contact(self):
        """Helpermethods for handling contact"""
        contact = self.data_manager.get_contact_info()
        return f"Du kannst mich unter {contact} erreichen."
