l = [1,2,3,4,5]
x = l # x zeigt auf die gleiche Liste wie l
a, *b = l # a = 1, b = [2, 3, 4, 5]
a = l[:1] # a = [1]
b = l[1:] # b = [2, 3, 4, 5]

x = 1; y = 2
y, x = x, y # tausch der Werte von x und y
# Früher: temp = x; x = y; y = temp
# Jetzt: x, y = y, x


# Beispiel für Listen/Tupel-Ergebnisse mit datetime:
from datetime import datetime
def get_date():
    return datetime.now().day, datetime.now().month, datetime.now().year    
tag, monat, jahr = get_date()
print(tag, monat, jahr)
