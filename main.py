import sys

from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice

from core.fifo import FIFO
from core.lru import LRU
from core.optimal import OPTIMAL
from lib.config import loadConfig, saveConfig
from lib.metadata import all_metadata
from lib.menu import (
    main_menu,
    settings_menu,
    string_input,
    toggle_options,
    integer_input,
)

if __name__ == "__main__":
    config = loadConfig()
    defaults = config["defaults"]
    settings = config["settings"]
    choice = main_menu(defaults["algo"])

    if choice >= 0:
        string = string_input(defaults["string"])

        if settings["remember_algo"]:
            defaults["algo"] = choice

        if settings["remember_string"]:
            defaults["string"] = string

        if settings["remember_algo"] or settings["remember_string"]:
            saveConfig(config)

        pages = list(map(int, string.strip().split()))

        if choice == 0:
            algorithm = FIFO(config, pages)
        elif choice == 1:
            algorithm = LRU(config, pages)
        elif choice == 2:
            algorithm = OPTIMAL(config, pages)

        algorithm.run()
    elif choice < 0:
        if choice == -1:
            setting = settings_menu(defaults["capacity"])

            if setting == 0:
                integer = integer_input(defaults["capacity"])
                defaults["capacity"] = int(integer)
                saveConfig(config)

                settings_menu(defaults["capacity"])
            elif setting == 1:
                options = toggle_options(
                    [settings["remember_algo"], settings["remember_string"]]
                )

                if len(options) > 0:
                    settings["remember_algo"] = options[0]
                    settings["remember_string"] = options[1]
                    saveConfig(config)

                    settings_menu(defaults["capacity"])
            elif setting == 2:
                saveConfig(
                    {
                        "defaults": {"string": "", "algo": 0, "capacity": 3},
                        "settings": {"remember_algo": True, "remember_string": True},
                    }
                )
            elif setting == 3:
                main_menu(defaults["algo"])
