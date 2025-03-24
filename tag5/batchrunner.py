import sys
import logging
import subprocess
from pathlib import Path

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("batch.log"),
        logging.StreamHandler()
    ]
)

def execute_command(cmd):
    logging.info(f"Starte Kommando: {cmd}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            logging.info(f"OK: {result.stdout.strip()}")
        else:
            logging.error(f"FEHLER (Code {result.returncode}): {result.stderr.strip()}")
    except subprocess.TimeoutExpired:
        logging.error(f"Kommando TIMEOUT: {cmd}")
    except Exception as e:
        logging.exception(f"Unerwarteter Fehler bei: {cmd}")

def main():
    command_file = sys.argv[1] if len(sys.argv) > 1 else "commands.txt angeben"

    if not Path(command_file).is_file():
        logging.error(f"Befehlsdatei nicht gefunden: {command_file}")
        return
    logging.info("Beginne Stapelverarbeitung")
    with open(command_file) as f:
        for line in f:
            cmd = line.strip()
            if cmd and not cmd.startswith("#"):
                execute_command(cmd)
    logging.info("Stapelverarbeitung abgeschlossen")

if __name__ == "__main__":
    main()
