import os

from date import current_time


def writing_in_log(text):
    file_path = os.path.dirname(__file__)
    file_path = file_path.split('gui')[0]
    file_path = file_path + r"\logfile.log"
    with open(file_path, "a") as log_file:
        log_file.write(current_time() +":" +   text + "\n")
