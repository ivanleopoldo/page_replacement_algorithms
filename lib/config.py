import json
import os


def loadConfig(
    configPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + "/config.json",
):
    with open(configPath, "r") as configFile:
        config = json.load(configFile)
    return config


def saveConfig(
    config,
    configPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + "/config.json",
):
    with open(configPath, "w") as configFile:
        json.dump(config, configFile, indent=4)
