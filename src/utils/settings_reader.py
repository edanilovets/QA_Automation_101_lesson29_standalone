import configparser
from pathlib import Path


class SettingsReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = Path(__file__).resolve().parent.parent.parent / "settings.ini"
        self.config.read(config_path)

    def get_base_ui_url(self, env: str = "qa"):
        return self.config[env].get("base_url_ui")