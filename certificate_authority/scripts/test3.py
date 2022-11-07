from interfaces.init import *
from deployment.Record import Record
from scripts.cleanFile import *
import multiprocessing
import time


def main():
    Record().get_record()
    # clean the file directory
    clean_file()
    # wait for record download
    time.sleep(9)
    Init().start_ui()

    # Record().get_record()
    # check_deployment_process = multiprocessing.Process(target=check_deployment)
    # run_process = multiprocessing.Process(target=run_main_program)
    # check_deployment_process.start()
    # run_process.start()


def check_deployment():
    while True:
        Record().get_record()
        time.sleep(1)


def run_main_program():
    Init().start_ui()
