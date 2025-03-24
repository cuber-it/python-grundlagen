import logging
from logging.handlers import RotatingFileHandler

# Rotierender File-Handler (max 1 MB, 3 Backups)
logfile = "batch.log"
handler = RotatingFileHandler(logfile, maxBytes=1_000_000, backupCount=3)

# Formatter
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)

# Root-Logger konfigurieren
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler,
        logging.StreamHandler()
    ]
)

logging.info("Dies ist ein Testeintrag für rollierendes Logging")
