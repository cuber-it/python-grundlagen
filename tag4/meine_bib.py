def mach_was():
    print("Mach was")

def tu_was(werte):
    print("Tu was mit", werte)
    return werte

def addiere(a, b):
    return a + b    

if __name__ == '__main__':
    print("Ich bin die Bibliothek")
    print("Ich werde nur ausgeführt, wenn ich direkt aufgerufen werde")
    print("z.B bei zusätzlicher standalone Nutzung")
    print("oder wenn hier Tests eingebaut werden")
    print("Ich werde nicht ausgeführt, wenn ich importiert werde")
    mach_was()
    tu_was("Hallo Welt")
    print(addiere(3, 4))
# End of meine_bib.py