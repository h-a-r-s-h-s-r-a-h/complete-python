import logging

# Configure the logging system
logging.basicConfig(
    filename="app.log",  # Specify the log file name
    filemode="w",  # Open the log file in write mode
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log message format
    datefmt="%Y-%m-%d %H:%M:%S",  # Define the date format
)
