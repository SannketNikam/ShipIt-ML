# The below code helps to directly call this file as a Python package instead of using from src.mlProject import logger
# But for some reason it not working so we are using it by src.mlProject

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
        level = logging.INFO,
        format = logging_str,

        handlers = [
            logging.FileHandler(log_filepath),
            logging.StreamHandler(sys.stdout)
        ]
)

logger = logging.getLogger("mlProjectLogger")