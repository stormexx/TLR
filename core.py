#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from platform import system
from traceback import print_exc
from typing import Any
from typing import Callable
from typing import List
from typing import Tuple
from colors import *


def clear_screen():
    if system() == "Linux":
        os.system("clear")
    if system() == "Windows":
        os.system("cls")


class TLR(object):
    # About the HackingTool
    TITLE: str = ""  # used to show info in the menu
    DESCRIPTION: str = ""

    INSTALL_COMMANDS: List[str] = []
    INSTALLATION_DIR: str = ""

    UNINSTALL_COMMANDS: List[str] = []

    RUN_COMMANDS: List[str] = []

    OPTIONS: List[Tuple[str, Callable]] = []

    def __init__(self, options=None, installable: bool = True,
                 runnable: bool = True, uninstallable: bool = True):
        if options is None:
            options = []
        if isinstance(options, list):
            self.OPTIONS = []
            if installable:
                self.OPTIONS.append(('Install', self.install))
            if uninstallable:
                self.OPTIONS.append(('Uninstall', self.uninstall))
            if runnable:
                self.OPTIONS.append(('Run', self.run))
        else:
            raise Exception(
                "OPTIONS MUST BE A LIST.")

    def show_info(self):
        desc = self.DESCRIPTION
        print("")
        os.system(f'echo "\t{desc}"|boxes -d cat | lolcat')
        print("")

    def show_options(self, parent=None):
        clear_screen()
        self.show_info()
        for index, option in enumerate(self.OPTIONS):
            print(f"[{index + 1}] {option[0]}")
        print(f"[{99}] Back to {parent.TITLE if parent is not None else 'Exit'}")

        option_index = input(light_red("\ntlr@stormex") + light_green(" »") + reset())

        try:
            option_index = int(option_index)
            if option_index - 1 in range(len(self.OPTIONS)):
                ret_code = self.OPTIONS[option_index - 1][1]()
                if ret_code != 99:
                    input("\n\n Press " + light_yellow("ENTER") + " to continue:")
            elif option_index == 99:
                if parent is None:
                    sys.exit()
                return 99


        except (TypeError, ValueError):
            print("Please enter a valid option")
            input("\n\n Press " + light_yellow("ENTER") + " to continue:")
        except Exception:
            print_exc()
            input("\n\n Press " + light_yellow("ENTER") + " to continue:")
        return self.show_options(parent=parent)

    def before_install(self):
        pass

    def install(self):
        self.before_install()
        if isinstance(self.INSTALL_COMMANDS, (list, tuple)):
            for INSTALL_COMMAND in self.INSTALL_COMMANDS:
                os.system(INSTALL_COMMAND)
            self.after_install()

    def after_install(self):
        print(light_green("\nSuccessfully installed!"))

    def before_uninstall(self) -> bool:
        """ Ask for confirmation from the user and return """
        return True

    def uninstall(self):
        if self.before_uninstall():
            if isinstance(self.UNINSTALL_COMMANDS, (list, tuple)):
                for UNINSTALL_COMMAND in self.UNINSTALL_COMMANDS:
                    os.system(UNINSTALL_COMMAND)
            self.after_uninstall()

    def after_uninstall(self):
        print(light_red("\nSuccessfully uninstalled!"))

    def before_run(self):
        pass

    def run(self):
        self.before_run()
        if isinstance(self.RUN_COMMANDS, (list, tuple)):
            for RUN_COMMAND in self.RUN_COMMANDS:
                os.system(RUN_COMMAND)
            self.after_run()

    def after_run(self):
        pass

    def is_installed(self, dir_to_check=None):
        print("Unimplemented: DO NOT USE")
        return "?"


class TLR_(object):
    TITLE: str = ""  # used to show info in the menu
    DESCRIPTION: str = ""
    TOOLS = []  # type: List[Any[TLR, TLR_]]

    def __init__(self):
        pass

    def show_info(self):
        os.system("figlet -f standard -c {} | lolcat".format(self.TITLE))
        # os.system(f'echo "{self.DESCRIPTION}"|boxes -d boy | lolcat')
        # print(self.DESCRIPTION)

    def show_options(self, parent=None):
        clear_screen()
        self.show_info()
        for index, tool in enumerate(self.TOOLS):
            print(f" [{index}] {tool.TITLE}")
        print(f" [{99}] {parent.TITLE if parent is not None else 'Exit'}")

        tool_index = input(light_red("\ntlr@stormex") + light_green(" »") + reset())

        try:
            tool_index = int(tool_index)
            if tool_index in range(len(self.TOOLS)):
                ret_code = self.TOOLS[tool_index].show_options(parent=self)
                if ret_code != 99:
                    input("\n\n Press " + light_yellow("ENTER") + " to continue:")
            elif tool_index == 99:
                if parent is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError):
            print("Please enter a valid option")
            input("\n\n Press " + light_yellow("ENTER") + " to continue:")
        except Exception as e:
            print_exc()
            input("\n\n Press " + light_yellow("ENTER") + " to continue:")
        return self.show_options(parent=parent)
