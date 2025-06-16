# Keine Parameterübergabe
def funktion_A():
    print("Funktion A")

# Optional 1 PArameter
def funktion_A1(optional=None):
    print("Funktion A1")
    print(f"Optionaler Parameter: {optional}")

funktion_A() # einzig erlaubter Aufruf
# funktion_A(4711) nicht erlaubt
funktion_A1() # erlaubt
funktion_A1(4711) # erlaubt

# 1 Pflichtparameter
def funktion_B(pflicht):
    print("Funktion B")
    print(f"Pflichtparameter: {pflicht}")

funktion_B(4711) # erlaubt
# funktion_B() # nicht erlaubt
# funktion_B(4711, 1234) # nicht erlaubt

# 2 Pflichtparameter
def funktion_C(pflicht1, pflicht2):
    print("Funktion C")
    print(f"Pflichtparameter 1: {pflicht1}")
    print(f"Pflichtparameter 2: {pflicht2}")

funktion_C(4711, 1234) # erlaubt
# funktion_C(4711) # nicht erlaubt
# funktion_C(4711, 1234, 5678) # nicht erlaubt
# funktion_C() # nicht erlaubt

# 1 Pflichtparameter, 1 optionaler Parameter
def funktion_D(pflicht, optional=None):
    print("Funktion D")
    print(f"Pflichtparameter: {pflicht}")
    if optional is not None:
        print("Optionaler Parameter ist gesetzt")

funktion_D(4711) # erlaubt
funktion_D(4711, 1234) # erlaubt
# funktion_D() # nicht erlaubt
# funktion_D(4711, 1234, 5678) # nicht erlaubt

# 1 Pflichtparameter, 1 optionaler Parameter mit Defaultwert
def funktion_E(pflicht, optional="Hallo"):
    print("Funktion E")
    print(f"Pflichtparameter: {pflicht}")
    print(f"Optionaler Parameter: {optional}")

funktion_E(4711) # erlaubt
funktion_E(4711, 1234) # erlaubt
# funktion_E() # nicht erlaubt
# funktion_E(4711, 1234, 5678) # nicht erlaubt

# 2 Pflicht, 2 Optionalparameter, davon 1 mit default-Wert
def funktion_F(pflicht1, pflicht2, optional1=None, optional2="Hallo"):
    print("Funktion F")
    print(f"Pflichtparameter 1: {pflicht1}")
    print(f"Pflichtparameter 2: {pflicht2}")
    print(f"Optionaler Parameter 1: {optional1}")
    print(f"Optionaler Parameter 2: {optional2}")

funktion_F(4711, 1234) # erlaubt
funktion_F(4711, 1234, 5678) # erlaubt
funktion_F(4711, 1234, 5678, "Hallo") # erlaubt
funktion_F(4711, 1234, optional2="Hallo") # erlaubt
# funktion_F() # nicht erlaubt
# funktion_F(4711) # nicht erlaubt
# funktion_F(4711, 1234, 5678, 1234, 5678) # nicht erlaubt
# funktion_F(4711, 1234, 5678, 1234, 5678, 1234) # nicht erlaubt
# funktion_F(4711, 1234, 5678, 1234, 5678, 1234, 1234) # nicht erlaubt
