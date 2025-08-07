import logging

logging.basicConfig(
    filename="scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_result(data):
    logging.info(f"Scan result: {data}")
