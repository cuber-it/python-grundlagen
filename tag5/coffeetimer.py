import csv
import time
from datetime import datetime
import tkinter as tk
from threading import Thread

CONFIG_FILE = "coffeetime.ini"
CHECK_INTERVAL = 30  # Sekunden

def load_schedule():
    schedule = {}
    with open(CONFIG_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            time_str = row["Time"].strip()
            message = row["Message"].strip()
            schedule[time_str] = message
    return schedule

def show_alert(message):
    root = tk.Tk()
    root.title("COFFEETIME!!!")
    label = tk.Label(root, text=f"☕ {message} ☕", font=("Helvetica", 24))
    label.pack(padx=50, pady=50)
    root.after(10000, root.destroy)  # Fenster nach 10 Sekunden schließen
    root.mainloop()

def alert_thread(message):
    t = Thread(target=show_alert, args=(message,))
    t.start()

def main():
    schedule = load_schedule()
    today_times = sorted(schedule.keys())
    if today_times:
        print(f"Letzter Coffee-Termin heute: {today_times[-1]}")
    else:
        print("Keine Coffee-Termine für heute gefunden.")

    notified_today = set()
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        schedule = load_schedule()
        if current_time in schedule and current_time not in notified_today:
            alert_thread(schedule[current_time])
            notified_today.add(current_time)

        if current_time == "00:00":
            notified_today.clear()

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
