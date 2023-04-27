#!/usr/bin/env python3

import shutil
import os


def main():

    # Force the program to start in the home user directory ---- allows the user to run the program from any location on the system
    os.chdir("/home/student/mycode")

    # Copy the file at the pth source to the folder at the path destination.
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # shutil.copy == copy single file.     shutil.copytree == copy an entire folder and EVERYTHING inside of it
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()


