from flaskr.constants import DATA_PATH, DATA_DIR
import os


def create_datafile() -> None:
    try:
        os.makedirs(DATA_DIR)
        file = open(DATA_PATH, "x")
        file.close()
    except OSError as error:
        pass
