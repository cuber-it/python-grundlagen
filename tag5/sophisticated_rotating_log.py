import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import time
import os
import gzip
import shutil

LOG_DIR = "logs"
LOG_FILE = "batch.log"
os.makedirs(LOG_DIR, exist_ok=True)

class CompressedTimedRotatingFileHandler(TimedRotatingFileHandler):
    def doRollover(self):
        super().doRollover()
        # Letztes Backup komprimieren
        if self.backupCount > 0:
            old_log = f"{self.baseFilename}.{self.rolloverAt - self.interval:%Y-%m-%d}"
            if os.path.exists(old_log):
                with open(old_log, 'rb') as f_in, gzip.open(f"{old_log}.gz", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                os.remove(old_log)

# Konfiguriere Handler
handler = CompressedTimedRotatingFileHandler(
    filename=os.path.join(LOG_DIR, LOG_FILE),
    when="midnight",
    interval=1,
    backupCount=14,
    encoding="utf-8",
    utc=False,  # True für UTC
    atTime=time(3, 0)  # Rollover um 03:00 Uhr
)

handler.setFormatter(logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))

# Root-Logger konfigurieren
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler,
        logging.StreamHandler()
    ]
)

logging.info("Erweitertes Logging mit Zeitsteuerung, Rotation & Kompression aktiv")
