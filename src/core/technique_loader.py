import importlib
import yaml
from pathlib import Path
from utils.logger import logger


class TechniqueLoader:
    def __init__(self, base_package="src.techniques"):
        self.base_package = base_package

    def load_from_profile(self, profile_path):
        profile_path = Path(profile_path)
        if not profile_path.exists():
            raise FileNotFoundError(f"Profile not found: {profile_path}")

        with profile_path.open("r", encoding="utf-8") as f:
            profile = yaml.safe_load(f)

        techniques_config = profile.get("techniques", [])
        techniques = []

        for item in techniques_config:
            module_path = item["module"]
            class_name = item.get("class", "Technique")
            meta = item.get("meta", {})

            technique = self._import_technique(module_path, class_name, meta)
            techniques.append(technique)

        logger.info("Loaded %d techniques from profile", len(techniques))
        return techniques

    def _import_technique(self, module_path, class_name, meta):
        """
        module_path: "discovery.T1087_list_users"
        """
        module_full = f"src.techniques.{module_path}"
        module = importlib.import_module(module_full)
        cls = getattr(module, class_name)
        instance = cls()
        instance.meta = meta
        return instance
