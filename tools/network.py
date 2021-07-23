#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from core import TLR
from core import TLR_


class Neter(TLR):
    TITLE = "Neter"
    DESCRIPTION = "Neter allows you to test the speed of your internet connection.\n"

    INSTALL_COMMANDS = [
        "git clone https://github.com/stormexx/Neter.git"
    ]
    RUN_COMMANDS = ["cd Neter && bash ./run.sh"]
    UNINSTALL_COMMANDS = ["sudo rm -r Neter"]

    def __init__(self):
        super(Neter, self).__init__([('Stop', self.stop)])

    def stop(self):
        os.system("exit")


class Network(TLR_):
    TITLE = "Network"
    DESCRIPTION = ""
    TOOLS = [
        Neter()
    ]
