import re

regex = r"\d\d:\d\d" # Match Uhrzeiten - als Suchmuster

test_str = ("# Time, Message\n" # Testdaten für das Beispiel hier
	"#09:00, First Coffee of the Day\n"
	"#09:30, Second Coffee of the Day\n"
	" \n"
	"#10:00, Third Coffee of the Day\n"
	"#10:30, Fourth Coffee of the Day\n"
	"#12:00, Midday Coffee\n\n"
	"#13:00, Afternoon Coffee\n"
	"#14:00, Afternoon Coffee\n"
	"#15:00, Afternoon Coffee\n"
	"#16:00, Afternoon Coffee\n"
	"#17:00, Afternoon Coffee")

matches = re.finditer(regex, test_str, re.MULTILINE) # Multiline-Modus, geht über alle Zeilen und findet jede Stelle

for matchNum, match in enumerate(matches, start=1):
    print("Gefunden: ", match.group()) # Ausgabe des gefundenen Musters

