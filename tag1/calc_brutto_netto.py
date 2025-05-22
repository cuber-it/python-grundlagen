#!/usr/bin/env python3
MWST = 0.19

brutto = float(input("Bruttobetrag: "))
netto = brutto / (1 + MWST)
mwst = brutto - netto

# Tabellarische Ausgabe für Report
print(f"{'Bruttobetrag':<20} {brutto:>10.2f}")
print(f"{'Netto':<20} {netto:>10.2f}")
print(f"{'MwSt':<20} {mwst:>10.2f}")
# Ausgabe in CSV-Format in Datei
with open("mwst.csv", "w") as f:
    f.write("Bruttobetrag;Netto\n")
    f.write(f"{brutto:.2f};{netto:.2f}\n")
