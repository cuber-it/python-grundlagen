# Keine Parameter
def funktion_1():
    print("Funktion 1")

def funktion_2(param1): # Pflichtparameter
    print("Funktion 2", param1)

def funktion_3(param1, param2): # 2 Pflichtparameter
    print("Funktion 3", param1, param2)

def funktion_4(param1, param2="Hallo"): # 1 Pflichtparameter, 1 Optionaler Parameter mit default-Wert
    print("Funktion 4", param1, param2)

# Aufruf ohne named parameters
funktion_4("Welt")
funktion_4("Welt", "Mars")

# Aufruf mit named parameters
funktion_4(param2="Mars", param1="Welt")
funktion_4(param1="Welt")
funktion_4(param1="Welt", param2="Mars")

# Für funktion_2 und funktion_3
# funktion_2() # Fehler: Funktion erwartet 1 Parameter
# funktion_2("Hallo")
# funktion_2(param1="Hallo")
#
# funktion_3() # Fehler: Funktion erwartet 2 Parameter
# funktion_3("Hallo", "Welt")   
# funktion_3(param1="Hallo", param2="Welt")
# funktion_3(param2="Welt", param1="Hallo")

def funktion_5(param1, param2=None, param3=0): # 1 Pflichtparameter, 2 Optionale Parameter
    print("Funktion 5", param1, param2, param3)

funktion_5("Hallo") # param2=None, param3=0
funktion_5("Hallo", "Welt") # param3=0
funktion_5("Hallo", "Welt", 42) # Kein default-Wert
funktion_5("Hallo", param3=42) # param2=None
funktion_5("Hallo", param2="Welt") # param3=0
funktion_5("Hallo", param3=42, param2="Welt") # Reihenfolge egal

# Funktion mit beliebig vielen Parametern
def funktion_6(*args):
    print("Funktion 6", args)   

def sum(*values):
    result = 0
    for value in values:
        result += value
    return result

print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(sum())
print(sum(1))

# Funktion mit beliebig vielen named parameters
def funktion_7(**kwargs): # kwargs = keyword arguments
    print("Funktion 7", kwargs)     

funktion_7(param1="Hallo", param2="Welt", param3=42)
funktion_7(param1="Hallo", param2="Welt")
funktion_7(param1="Hallo")
funktion_7()

# alle Kombinationen
def funktion_8(param1, param2, param3=None, param4=0, *args, **kwargs):
    print("Funktion 8", param1, param2, param3, param4, args, kwargs)

funktion_8("Hallo", "Welt", 42, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, param5="Mars", param6="Venus")
funktion_8( "Hallo", "Welt", 42, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, param5="Mars")
funktion_8("Hallo", "Welt", 42, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
funktion_8("Hallo", "Welt", 42, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, param5="Mars", param6="Venus")
funktion_8("Hallo", "Welt", 42, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, param6="Venus")

