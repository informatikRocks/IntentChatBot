import json
import os

class DataManager:
    def __init__(self):
        # Determine the path to profile.json relative to this file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(base_dir, "data", "profile.json")
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            return {}

    def get_projects(self, tech_filter=None):
        projects = self.data.get("projects", [])
        if not tech_filter:
            return projects
        
        filtered = []
        for p in projects:
            stack = [t.lower() for t in p.get("tech_stack", [])]
            if tech_filter.lower() in stack:
                filtered.append(p)
        return filtered

    def get_contact_info(self):
        profile = self.data.get("profile", {})
        return profile.get("contact", "Keine Kontaktinfo verfügbar.")
