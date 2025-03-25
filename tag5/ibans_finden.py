import re

regex = r"^IBAN.*$"

test_str = ("Sehr geehrte Damen und Herren,\n\n"
	"bitte überweisen Sie den fälligen Betrag auf eines der folgenden Konten:\n\n"
	"Konto Deutschland:\n"
	"IBAN: DE44 5001 0517 5407 3249 31\n"
	"BIC: INGDDEFFXXX\n\n"
	"Konto Österreich:\n"
	"IBAN: AT61 1904 3002 3457 3201\n"
	"BIC: BAWAATWW\n\n"
	"Konto Schweiz:\n"
	"IBAN: CH93 0076 2011 6238 5295 7\n"
	"BIC: UBSWCHZH80A\n\n"
	"Konto Niederlande:\n"
	"IBAN: NL91 ABNA 0417 1643 00\n"
	"BIC: ABNANL2A\n\n"
	"Alternativ nutzen Sie bitte unser Geschäftskonto:\n"
	"IBAN: DE98 7654 3210 0000 1234 56\n"
	"BIC: GENODEF1S01\n\n"
	"Vielen Dank für Ihre Zahlung.\n\n"
	"Mit freundlichen Grüßen\n"
	"Kundendienst Finanzen")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print("Gefunden: ", match.group())
    if match.group().startswith("IBAN: DE"):
        print("Deutsche IBAN gefunden!", match.group())