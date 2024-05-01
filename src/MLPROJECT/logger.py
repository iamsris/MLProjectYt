import logging
import os
from datetime import datetime

# Define log directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_file = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"
log_file_path = os.path.join(log_dir, log_file)

# Set up logging configuration
logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Example usage
logging.info("Logging started")
