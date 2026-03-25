import logging
from logging.handlers import RotatingFileHandler

file = RotatingFileHandler("app.log", maxBytes=500, backupCount=1)

console = logging.StreamHandler()

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[file, console],
    format="%(levelname)s:%(message)s"
)

def parse(f):
    try:
        for i, line in enumerate(open(f), 1):
            line = line.strip()
            logging.debug(line)
            logging.info(line.split(",")) if line else logging.warning("Empty")
    except FileNotFoundError:
        logging.error("Apple")

parse("data.txt")
parse("missing.txt")