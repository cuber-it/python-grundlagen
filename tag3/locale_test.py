import locale
import time

# Set locale to German (Germany)
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

# Format current date
formatted_date = time.strftime("%A, %d. %B %Y")
print(formatted_date)  # Example: Montag, 26. Februar 2025
