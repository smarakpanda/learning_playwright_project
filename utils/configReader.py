import configparser

from utils.decorators.LoggingDecorator import log_decorator


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(r"C:\Users\smara\PycharmProjects\PythonProject\config.properties")

    @log_decorator
    def get_value_from_config(self,key,section="DEFAULT"):
        return self.config[section][key]


if __name__ == "__main__":
    config = ConfigReader()
    print(config.get_value_from_config("headless",))



