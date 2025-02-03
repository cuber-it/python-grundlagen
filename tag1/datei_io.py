#!/usr/bin/env python3
import os

# unter Windows "nativ": r"C:\Users\ucuber\Workspace\kurse\python-grundlagen\materialien\Sample.log"
# unter Linux "nativ":   "/home/ucuber/Workspace/kurse/python-grundlagen/materialien/Sample.log"
quelle = r"/home/ucuber/Workspace/kurse/python-grundlagen/materialien/Sample.log"

# Datei lesen
fd = open(quelle, 'r') # das 'r' kann weggelassen werden, da es der Default-Wert ist
# Daten aus Datei lesen
text = fd.read()
# Datei schliessen
fd.close()

# Kurzform: - Insidername: slurp (schlürfen)
# with open(quelle, 'r') as fd:
#     text = fd.read()

print(text[:500])  # nur die ersten 500 Zeichen anzeigen
print("Länge des Textes:", len(text))

# Schreiben in eine Datei
ziel = os.path.join(os.path.dirname(quelle), "Sample.txt")
print("Ziel:", ziel)

# Insidername: spew (speien)
with open(ziel, 'w') as fd:
    fd.write(text)