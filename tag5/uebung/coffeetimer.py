# Coffeetimer
#
# Dies Anwendung wird morgens gestart - erst Amtshandlung! - und zeigt an, wann der Kaffee fertig ist.
# Es wird eine Zeit in Minuten eingegeben und die Anwendung zählt die Zeit runter.
# Wenn die Zeit abgelaufen ist, wird eine Nachricht ausgegeben.
#
# Hinweis: time.sleep(), threading.Thread, tkinter
#
# Aufruf: coffeetimer.py Feierabendzeit als hh:mm coffeeconfig.ini
#
# Beispiel: coffeetimer.py 16:30 coffeeconfig.ini
#
# coffeeconfig.ini:
# Time, Message
#09:00, First Coffee of the Day
#09:30, Second Coffee of the Day
#10:00, Third Coffee of the Day
#10:30, Fourth Coffee of the Day
#12:00, Midday Coffee
#13:00, Afternoon Coffee
#14:00, Afternoon Coffee
#15:00, Afternoon Coffee
#16:00, Afternoon Coffee
#17:00, Afternoon Coffee
#
#
# MEldungsausgabe auf der Kommandozeile (einfache Version)
# Wer Lust hat gibt mit tkinter eine grafische Meldung aus (Copilot fragen)
#
import sys
import time
import threading

from datetime import datetime, timedelta

# Umwandlung in datetime-Objekt (nur Uhrzeit)
def as_time_object(today, time_str):
    t = datetime.strptime(time_str, "%H:%M")
    return t.replace(year=today.year, month=today.month, day=today.day)
 
def time_delta(time_obj_a, time_obj_b):
    return time_obj_a - time_obj_b

def load_coffeetimes(filename):
    today = datetime.today()
    with open(filename, "r") as f:
        coffeetimes = {}
        for line in f[1:]:
            time, message = line.strip().split(",")
            coffeetimes[as_time_object(today, time)] = message
        return coffeetimes

def run_timer(coffeetimes, endtime):
    times = sorted(coffeetimes.keys())
    now = datetime.now()

    # Schon Feierabend?
    if now > endtime:
        return

    # vergangene Zeiten überspringen
    coffeetimes = {time: msg for time, msg in coffeetimes.items() if time > now}

    # Bis Feierabend ist Kaffeezeiten auswerten, 
    # wenn noch welche übrig sind
    for coffeetime in sorted(coffeetimes.keys()):
        now = datetime.now()

        if endtime <= now or coffeetime > endtime:
            return

        delta = time_delta(coffeetime, now)
        sleep_seconds = delta.total_seconds()

        time.sleep(sleep_seconds)
        print(f"COFFEETIME @ {coffeetime.strftime('%H:%M')} — {coffeetimes[coffeetime]}")

    # nach letzter Kaffeezeit ggf. bis Feierabend warten
    now = datetime.now()
    if now < endtime:
        delta = time_delta(endtime, now)
        time.sleep(delta.total_seconds())

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Aufruf: coffeetimer.py <Feierabendzeit als hh:mm> <coffeeconfig.ini>")
        sys.exit(1)

    feierabend = as_time_object(sys.argv[1])
    try:
        coffeetimes = load_coffeetimes(sys.argv[2])
        run_timer()
        print("Feierabend! Bis morgen!")
        sys.exit(0)
    except FileNotFoundError:
        print(f"Datei {sys.argv[2]} nicht gefunden!")
        sys.exit(1)