# Bulkrename
# 1. Alle Dateien in einem Verzeichnis auflisten
# 2. Neue Dateinamen generieren
# 3. Dateien umbenennen
#
# Dateinamen: datei1.txt, datei2.txt, datei3.txt, ...
# Neuer Name: datei_1.txt, datei_2.txt, datei_3.txt, ...
#
# Hinweis: os.listdir(), os.rename(), glob.glob()
#
# Aufruf: bulkrename.py 'datienamensmuster' 'altert_namensbestandteil, 'ersetzung'
#
# Beispiel: bulkrename.py 'datei*' 'Datei' 'datei_' # datei1.txt -> datei_1.txt, datei2.txt -> datei_2.txt, ...
#
# Das sind verändernde Befehl. Ich habe immer ein flag -n als dryrun, soll heissen es wird nur ausgedruckt was passieren würde, wenn dieses flag nicht gesetzt ist.

import os
import glob
import sys

def bulkrename(filepattern, oldpart, replacement, dryrun=False):
    for filename in glob.glob(filepattern):
        newname = filename.replace(oldpart, replacement)
        if newname != filename:
            if dryrun:
                print(f"Umbenennen von {filename} in {newname}")
            else:
                os.rename(filename, newname)

if __name__ == "__main__":
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Aufruf: bulkrename.py [-n] 'dateinamensmuster' 'alter_namensbestandteil, 'ersetzung'")
        sys.exit(1)
    
    # Dryrun Flag gesetzt? True/False
    dryrun = "-n" in sys.argv

    # Wenn Flag gesetzt, entfernen, es bleiben nur die Argumente
    if dryrun:
        sys.argv.remove("-n")

    # Argumente zuweisen
    filepattern = sys.argv[1]
    oldpart = sys.argv[2]
    replacement = sys.argv[3]
    
    bulkrename(filepattern, oldpart, replacement, dryrun)