import logging
from logging.handlers import TimedRotatingFileHandler

# Log-Datei mit täglichem Rollover, 7 Backups behalten
handler = TimedRotatingFileHandler(
    "batch.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)

handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler,
        logging.StreamHandler()
    ]
)

logging.info("Tägliches rollierendes Logging aktiviert")
