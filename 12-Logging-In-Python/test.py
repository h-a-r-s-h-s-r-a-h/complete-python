from logger import logging


def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

logging.info("Starting the addition process")
add(10, 20)
