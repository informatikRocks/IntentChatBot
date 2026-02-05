
from .data_manager import DataManager


class IntentHandler:
    def __init__(self):
        self.data_manager = DataManager()

    def handle_intent(self, nlp_analysis):
        entities = nlp_analysis.get("entities", [])
        
        detected_intents = [label for text, label in entities]
        
        tech_filter = next((text for text, label in entities if label == "TECH"), None)


        print(f"Erkannt: {detected_intents}, Tech: {tech_filter}")

       
        if "INTENT_KONTAKT" in detected_intents:
            return self._handle_contact()
        
        if "INTENT_PROFILE" in detected_intents:
            return self._handle_profile()

       
        if "INTENT_PROJEKTE" in detected_intents or tech_filter:
            return self._handle_projects(tech_filter)
        
        if "INTENT_SKILLS" in detected_intents:
            return self._handle_skills()
        
        if "INTENT_HOBBIES" in detected_intents:
            return self._handle_hobbies()
        
        return "Ich verstehe nicht ganz. Kannst du das anders formulieren?"

 
    def _handle_profile(self):
        name = self.data_manager.data.get("profile", {}).get("name", "Unbekannt")
        role = self.data_manager.data.get("profile", {}).get("role", "Entwickler")
        return f"Ich bin der Bot von {name}, einem {role}."


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
    
    def _handle_skills(self):
        pass

    def _handle_hobbies(self): 
        pass
