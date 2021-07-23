# coding=utf-8
import os

from core import TLR
from core import TLR_


class Biner(TLR):
    TITLE = "Biner"
    DESCRIPTION = "Biner for looking up credit and debit card metadata.\n"

    INSTALL_COMMANDS = [
        "git clone https://github.com/stormexx/Biner.git",
        "cd Biner && chmod +x install.sh && bash ./install.sh"

    ]
    RUN_COMMANDS = ["cd Biner && bash ./run.sh"]
    UNINSTALL_COMMANDS = ["sudo rm -r Biner"]

    def __init__(self):
        super(Biner, self).__init__([('Stop', self.stop)])

    def stop(self):
        os.system("exit")


class Profiler(TLR):
    TITLE = "Profiler"
    DESCRIPTION = "Profiler allows you to have access to the information of any instagram user.\n"

    INSTALL_COMMANDS = [
        "git clone https://github.com/stormexx/Profiler.git",
        "cd Profiler && chmod +x install.sh && bash ./install.sh"

    ]
    RUN_COMMANDS = ["cd Profiler && bash ./run.sh"]
    UNINSTALL_COMMANDS = ["sudo rm -r Profiler"]

    def __init__(self):
        super(Profiler, self).__init__([('Stop', self.stop)])

    def stop(self):
        os.system("exit")


class Viewers(TLR_):
    TITLE = "Viewers"
    DESCRIPTION = ""
    TOOLS = [
        Biner(),
        Profiler()
    ]
