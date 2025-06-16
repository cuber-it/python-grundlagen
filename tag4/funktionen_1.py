# Eingabefunktion(en)
def read_vorname():
    return input("Vorname: ")
    
def read_nachname():
    return input("Nachname: ")

# Verarbeitungfunktion(en)
def verarbeitung(vname, nname):
    return f"{vname} {nname}"

# Ausgabefunktion(en)
def write_hello(text):
    print("Hello ", text)

# Hauptfunktion
def hello():
    print("Hallo, ich bin ein Programm.")
    print("Ich kann Vorname und Nachname verarbeiten.")

    # Eingabe    
    vname = read_vorname()
    nname = read_nachname()

    # Verarbeitung
    text = verarbeitung(vname, nname)
    
    # Ausgabe
    write_hello(text)
    
    print("Das war's auch schon.")
    print("Auf Wiedersehen!")

# Aufruf der Hauptfunktion => "Programmstart"
hello()