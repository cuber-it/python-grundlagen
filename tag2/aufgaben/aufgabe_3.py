# Aufgabe:
#
# Ein Fahrkartenautmat soll gebaut werden
#
# Der Benutzer soll ein Ticket wählen aus den verfügbaren:
# - Kleine Fahrt: 1,80
# - Große Fahrt: 2,50
# - Tageskarte: 4,00
#
# Der Automat ist immer aktiv!
# Der Benutzer wählt aus, aus dem Angebot
# Der Benutzer gibt Geld ein - so lange bis der Zielbetrag erreicht ist oder überschritten
# Der Automat gibt das Ticket aus und das Wechselgeld
#
# Erlaubte Eingabebeträge:
# - 0,10
# - 0,20
# - 0,50
# - 1,00
# - 2,00
# Keine weiteren Beträge sind erlaubt
#
# Der Automat kann nur an den Geschäftszeiten aktiv sein: 05:00 - 22:00
# Außerhalb dieser Zeiten soll eine der Automat abgeschaltet sein
#
# Hinweis:
# - Verwendet eine zeitgesteuerte Schleife
# - Verwendet eine Fehlerbehandlung für die Eingabe
# - Weiss wann "jetzt" ist und kann das mit den Geschäftszeiten vergleichen
# - "jetzt" in python: https://docs.python.org/3/library/datetime.html
# - "Zeitvergleich in Python": https://www.w3schools.com/python/python_datetime.asp
#
import datetime
import decimal

KLEINE_FAHRT = 1.80 # besser wäre insgesamt: decimal.Decimal("1.80")
GROSSE_FAHRT = 2.50
TAGESKARTE   = 4.00

opening = datetime.time(5, 0, 0)
closed  = datetime.time(22, 0, 0)

actual_time = datetime.datetime.now().time()

while actual_time >= opening and actual_time <= closed:
  # Bildschirm clearen
  print("\033[2J\033[H", end='') # ANSI Escape Sequenz
  print("TICKETAUTOMAT (AlphaTick 0.1)")
  print("="*40)
  print(f"(a) Kleine Fahrt: {KLEINE_FAHRT:>10.2f}")
  print(f"(b) Große Fahrt:  {GROSSE_FAHRT:>10.2f}")
  print(f"(c) Tageskarte:   {TAGESKARTE:>10.2f}")
  print("="*40)
  auswahl = input("Ihre Auswahl (a/b/c): ").lower()

  if auswahl == "a":
    ticket = KLEINE_FAHRT
  elif auswahl == "b":
    ticket = GROSSE_FAHRT
  elif auswahl == "c":
    ticket = TAGESKARTE
  else:
    input("Fehler: Ungültige Auswahl. Weiter mit ENTER")
    continue
  
  eingeworfen = 0
  while eingeworfen < ticket:
    betrag = input("Bitte werfen Sie Geld ein (0,10/0,20/0,50/1,00/2,00): ")
    try:
      betrag = float(betrag.replace(",", ".")) # 0,10 -> 0.10
      if betrag == 0.10 or betrag == 0.20 or betrag == 0.50 or betrag == 1.00 or betrag == 2.00:
        eingeworfen += betrag
        print(f"Bisher eingeworfen: {eingeworfen:.2f}")
      else:
        input("Fehler: Ungültiger Betrag. Weiter mit ENTER")
    except ValueError:
      input("Fehler: Bitte geben Sie eine Zahl ein. Weiter mit ENTER")      

  print("Ihr Ticket entnehmen")

  if eingeworfen > ticket:
    print(f"Ihr Wechselgeld: {eingeworfen - ticket:.2f}")

  input("Weiter mit ENTER")

  actual_time = datetime.datetime.now().time()

print("Automat ist außerhalb der Geschäftszeiten geschlossen.")
