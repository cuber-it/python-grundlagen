datei_name = r'/home/ucuber/Workspace/kurse/python-grundlagen/materialien/small_sample.log'

# E ingabe
with open(datei_name) as datei:
    zeilen = datei.read().splitlines() # zerlegt und beseitigt das '\n' am Ende jeder Zeile


# V erarbeitung
anz_info = 0
for zeile in zeilen:
    if 'INFO' in zeile:
        anz_info += 1
        if anz_info == 24:
            worte = zeile.split(' ')
            # die comprehension entfernt alle Leerzeichen
            # und leere Strings
            # worte = [wort for wort in worte if wort.strip() != '']
            worte_neu = []
            for wort in worte:
                if wort.strip() != '':
                    worte_neu.append(wort)
            worte = worte_neu

# A usgabe
print(len(zeilen))
print(anz_info)
print(worte)
