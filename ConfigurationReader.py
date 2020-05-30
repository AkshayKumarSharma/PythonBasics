import configparser

class ConfigurationReader :
    
    # this is called constructor and it is called automatically on object creation
    # it is used to initialize the basic state of an object, like initializing few properties
    def __init__(self):     
        print('ConfigurationReader called.')        
        self.configurationFilePath = r'.\configs\configurations.ini'

    def FetchValue(self, section,key):
        # usage of configparser library to ini file
        configParser = configparser.RawConfigParser()   
        # Example of string interpolation
        print(f'Configuration file path : {self.configurationFilePath}') 
        # here ini file is being read
        configParser.read(self.configurationFilePath)
        # here the value of asked key from section is returned to calling function
        return configParser.get(section, key)