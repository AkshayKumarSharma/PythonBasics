import configparser

class ConfigurationReader :
    def FetchValue(self, section,key):
        configParser = configparser.RawConfigParser()   
        configFilePath = r'.\configurations.ini'
        configParser.read(configFilePath)
        return configParser.get(section, key)