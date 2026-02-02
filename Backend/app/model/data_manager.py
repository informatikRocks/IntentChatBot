import json
from pathlib import Path

class DataManager:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent / "data"
        self.data = self._load_profile_data()

    def _load_profile_data(self):
        json_path = self.base_dir / "profile.json"
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {json_path} not found")
            return {"profile": {}, "projects": []} # Fallback, damit es nicht crasht

    def get_contact_info(self):
        return self.data["profile"].get("contact", "Keine Info")

    def get_projects(self, tech_filter=None):
        projects = self.data.get("projects", []) 
        if tech_filter:
            return [p for p in projects if tech_filter.lower() in [t.lower() for t in p.get("tech_stack", [])]]
        return projects