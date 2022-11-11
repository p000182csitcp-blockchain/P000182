from interfaces.init import *
from scripts.cleanFile import *


def main():
    # clean the file directory
    clean_file()
    # wait for record download
    Init().start_ui()
