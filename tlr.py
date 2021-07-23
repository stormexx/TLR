##!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from platform import system
from time import sleep
from core import TLR_
from tools.viewers import Viewers
from tools.network import Network
from colors import *
from banner import logo

all_tools = [
    Viewers(),
    Network()
]


class TLR_Tools(TLR_):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        logo()


if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = "tlr.txt"
            if not os.path.exists(fpath):
                os.system('clear')
                # run.menu()
                print("""SET PATH FOR TOOLS
                
                        [1] Default (home)""")
                choice = input(light_red("\ntlr@stormex") + light_green(" »") + reset())

                if choice == "1":
                    autopath = "tlr/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print(f"DEFAULT PATH : {autopath}")
                    sleep(3)
                else:
                    print("ERROR...")
                    exit(0)

            with open(fpath) as f:
                archive = f.readline()
                if not os.path.exists(archive):
                    os.mkdir(archive)
                os.chdir(archive)
                all_tools = TLR_Tools()
                all_tools.show_options()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print("\033[91m RUN IT ON LINUX \33e[00m")
            sleep(1)

        else:
            print("ERROR...")

    except KeyboardInterrupt:
        sleep(1)
