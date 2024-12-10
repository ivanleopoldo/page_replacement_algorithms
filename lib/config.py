import json


def loadConfig(configPath="config.json"):
    with open(configPath, "r") as configFile:
        config = json.load(configFile)
    return config


def saveConfig(config, configPath="config.json"):
    with open(configPath, "w") as configFile:
        json.dump(config, configFile, indent=4)
