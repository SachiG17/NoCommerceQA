#  In order to read the info in the config.ini we need to create teh methods and
# class in this read peroperties file

import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getUrl():
        url = config.get('common info', 'url')
        return url
    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username
    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password