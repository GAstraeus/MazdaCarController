import configparser


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_key = config['Default']['api_key']
        self.username = config['Default']['username']
        self.password = config['Default']['password']