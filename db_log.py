import logging

# Configure logging to write to a log file
log_filename = "postgres_setup.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
