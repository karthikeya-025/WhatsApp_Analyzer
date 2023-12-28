import logging
import datetime
import os

LOG_FILE = f'{datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

log_file_path = os.path.join(os.getcwd(),'logs',LOG_FILE)

os.makedirs(log_file_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_file_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


