
import logging
from filecontextmnger import filecontextmnger

logging.basicConfig(
filename='files.log',
level=logging.INFO,
format='%(asctime)s-%(levelname)s-%(message)s'
)


def filereader(filename):
    with filecontextmnger(filename,'r') as file:
        if file:
            contents = file.read()
            logging.info("File has been opened")
            return contents
        else:
            logging.error("File could not be opened")
            return None





