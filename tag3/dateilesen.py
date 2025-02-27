# Wir bauen einen Logreport. 
# Zu allen message_typen werden die Logzeilen gesammelt
# und am Ende die Anzahl der Zeilen ausgegeben.
import pprint

logfile = r"materialien/Sample.log"

with open(logfile, "r") as file:
    rows = file.read().splitlines()

report_daten = {}

for row in rows:
    message_key = row.split(":")[2].split()[1]
    
    if message_key in report_daten.keys():
        report_daten[message_key] += 1
    else:
        report_daten[message_key] = 1

pprint.pprint(report_daten, width=40, indent=2)

