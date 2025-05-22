import configparser
import os

class Config:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', config_file)
        self.config.read(config_path)

    def get(self, section, key):
        return self.config.get(section, key)
