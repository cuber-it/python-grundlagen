def mach_was(name):
    print("Hello", name)
    return 0
    
def tu_was(namen): # namen ist lokale Variable und Parameter
    namen = ["X", "Y", "Z" ] # lokale Variable wird neu belegt - löst übergebene Liste ab
    counter = 0 # lokale Variable
    for name in namen: # name ist eine lokale Variable
        mach_was(name)
        counter += 1
    return counter
    
namen = ["Willi", "Heinz", "Karl"]   # globale Variable
ausgegeben = tu_was(namen)
print("Anzahl der ausgegebenen Namen:", ausgegeben)