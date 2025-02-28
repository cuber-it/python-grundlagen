# Filefinder:
#
# Schreiben Sie ein Programm, das in einem Verzeichnis 
# rekursiv nach Dateien sucht, die einem bestimmten 
# Muster entsprechen.

# Berechnen Sie für jede Datei, die dem Muster entspricht, 
# deren md5 Hashwert.

# Geben Sie eine Protokolldatei aus, in der Dateiname, Pfad, 
# md5-Wert ausgegeben werden für alle gefundnen Dateien
import os
import sys
import fnmatch
import hashlib
from typing import List, Dict

def calc_md5(file: str) -> str:
    """
    Berechnet den MD5-Hashwert einer Datei
    :param file: Dateiname
    :return: MD5-Hashwert
    """
    with open(file, "rb") as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()

def find_files(directory: str , pattern: str) -> Dict: # Pattern: *.txt
    """
    Sucht Dateien in einem Verzeichnis, die einem bestimmten Muster entsprechen
    :param directory: Verzeichnis
    :param pattern: Muster
    :return: Liste der gefundenen Dateien
    """
    result = [] # Liste für die gefundenen Dateien anlegen
    for root, _, files in os.walk(directory): # Verzeichnis rekursiv durchsuchen
        for name in files:
            if fnmatch.fnmatch(name, pattern): # Datei gefunden
                result.append(os.path.join(root, name)) # Datei hinzufügen
    return result

def build_report_data(files: List) -> Dict:
    """
    Erstellt die Daten für den Report
    :param files: Liste der Dateien
    :return: Dictionary mit Dateiname, Pfad und MD5-Hashwert
    """
    result = {}
    for file in files:
        md5 = calc_md5(file)
        fname = os.path.basename(file)
        path = os.path.dirname(file)
        result[fname] = { 'path': path, 'hash': md5 }
    return result

def create_report(report_data: Dict, report_file: str):
    """
    Erstellt den Report
    :param report_data: Dictionary mit Dateiname, Pfad und MD5-Hashwert
    :param report_file: Dateiname für den Report
    """
    with open(report_file, "w") as f:
        for file, data in report_data.items():
            f.write(f"{file}, {data['path']}, {data['hash']} \n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python file_finder.py <start> <pattern> <report_file>")
        sys.exit(1)
    start = sys.argv[1]
    pattern = sys.argv[2]
    report_file = sys.argv[3]

    files = find_files(start, pattern)
    if len(files) == 0:
        print("Keine Dateien gefunden")
        exit(0)
    report_data = build_report_data(files)  
    create_report(report_data, report_file)
    print("Report erstellt")
    exit(0)
# Aufruf: python file_finder.py
