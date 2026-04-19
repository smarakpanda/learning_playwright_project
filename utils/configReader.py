import os
import configparser
from utils.decorators.LoggingDecorator import log_decorator


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
        config_path = os.path.join(project_root, "config.ini")

        print("Reading config from:", config_path)
        print("Exists?", os.path.exists(config_path))

        files_read = self.config.read(config_path)

        if not files_read:
            raise FileNotFoundError(f"Config file not found at {config_path}")

    @log_decorator
    def get_value_from_config(self, key, section="DEFAULT"):
        try:
            return self.config[section][key]
        except KeyError:
            raise Exception(f"Missing '{key}' in section '{section}' of config.ini")