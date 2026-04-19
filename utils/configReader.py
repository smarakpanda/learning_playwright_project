import os
import configparser

class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
        config_path = os.path.join(project_root, "config.ini")

        print("Reading config from:", config_path)
        print("Exists?", os.path.exists(config_path))

        self.config.read(config_path)