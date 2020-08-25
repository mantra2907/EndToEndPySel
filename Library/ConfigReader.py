import configparser

def readconfigData(section,key):
    config =configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    #config.read("../ConfigurationFiles/Config.cfg")
    return config.get(section,key)

#print(readconfigData('Details','Application_URL'))

def readElementData(section,key):
    config=configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section,key)

#print(readElementData('Registration','user_name'))