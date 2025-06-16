# Beliebig lange Werteliste
def funktion_a(*x):
    print("Funktion A")
    print(f"Parameter: {x}")
    print(f"Anzahl Parameter: {len(x)}")
    for i in x:
        print(i)
    print("Ende Funktion A")

funktion_a(4711, 1234, 5678) # erlaubt
funktion_a(4711) # erlaubt
funktion_a() # erlaubt
funktion_a(1,2,3,4,5,6,7,8,9,10) # erlaubt


# Beliebige Anzahl von key=value Paaren
def funktion_b(**x):
    print("Funktion B")
    print(f"Parameter: {x}")
    print(f"Anzahl Parameter: {len(x)}")
    for key, value in x.items():
        print(f"{key}: {value}")
    print("Ende Funktion B")

funktion_b(vorname="Hans", nachname="Müller", plz=4711, ort="München") # erlaubt
funktion_b(vorname="Hans", nachname="Müller") # erlaubt
funktion_b() # erlaubt
# ODer zur Simulation beleibiger optionale Parameter in named parameter Schreibweise

# Man kann alles mit allem kombinieren, solange bestimmte Reihenfolge eingehalten wird
def funktion_c(pflicht, *x, optional=None, **y):
    print("Funktion C")
    print(f"Pflichtparameter: {pflicht}")
    print(f"Optionaler Parameter: {optional}")
    print(f"Parameter: {x}")
    print(f"Parameter: {y}")
    print("Ende Funktion C")

funktion_c(4711, 1234, 5678, optional="Hallo", vorname="Hans", nachname="Müller") # erlaubt
funktion_c(4711, 1234, 5678, vorname="Hans", nachname="Müller") # erlaubt
funktion_c(4711, 1234, optional="Hallo", vorname="Hans", nachname="Müller") # erlaubt
funktion_c(4711, 1234, 5678) # erlaubt
