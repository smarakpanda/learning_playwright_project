import configparser

from utils.decorators.LoggingDecorator import log_decorator
import os


class ConfigReader:

    def __init__(self):

        print("CWD:", os.getcwd())
        print("Files in CWD:", os.listdir())

        self.config = configparser.ConfigParser()
        self.config.read(r"C:\Users\smara\PycharmProjects\PythonProject\config.properties")

    @log_decorator
    def get_value_from_config(self,key,section="DEFAULT"):
        return self.config[section][key]


if __name__ == "__main__":
    config = ConfigReader()
    print(config.get_value_from_config("headless",))



