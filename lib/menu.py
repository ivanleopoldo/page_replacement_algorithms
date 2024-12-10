from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from .metadata import all_metadata


def main_menu(default):
    choice = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        message="Which algorithm would you like to use?",
        choices=[
            Choice(index, name=metadata["name"])
            for index, metadata in enumerate(all_metadata)
        ]
        + [Choice(len(all_metadata), "All"), Separator(), Choice(-1, name="Settings")],
        default=default,
    ).execute()
    return choice


def string_input(default):
    string = inquirer.text(
        raise_keyboard_interrupt=False,
        mandatory=False,
        message="Enter the reference string (separate using spaces):",
        default=str(default),
    ).execute()
    return string


def settings_menu(default):
    setting = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        message="Settings",
        default=0,
        choices=[
            Choice(0, name=f"Memory Capacity (CURRENT: {default})"),
            Choice(1, name="Toggle Options"),
            Choice(2, name="Reset to defaults"),
            Separator(),
            Choice(3, name="Back"),
        ],
    ).execute()
    return setting


def integer_input(default):
    integer = inquirer.number(
        raise_keyboard_interrupt=False,
        mandatory=False,
        message="Enter Memory Capacity:",
        default=default,
    ).execute()
    return integer


def toggle_options(defaults):
    options = inquirer.checkbox(
        raise_keyboard_interrupt=False,
        message="Toggle Options",
        mandatory=False,
        default=0,
        choices=[
            Choice(
                0,
                name="Remember Last Used Algorithm",
                enabled=defaults[0],
            ),
            Choice(
                1,
                name="Remember String",
                enabled=defaults[1],
            ),
        ],
    ).execute()

    ret = [False, False]

    for i in options:
        ret[i] = defaults[i] == True

    return ret
