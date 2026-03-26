import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"  #This will create a log file with the current date and time as its name
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # This will create a path for the log file in a "logs" directory within the current working directory
os.makedirs(logs_path, exist_ok=True) # This will create the "logs" directory if it doesn't already exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # This will create the full path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH, # This specifies the file where the logs will be written
    format="[%(asctime)s] %(levelname)s - %(message)s", # This specifies the format of the log messages
    level=logging.INFO # This specifies the logging level
)

if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")
    