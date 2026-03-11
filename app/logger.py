import logging

logging.basicConfig(
    filename="sales.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(msg):
    logging.info(msg)