def mach_was(name):
    print("Hello", name)
    return 0
    
def tu_was(namen):
    for name in namen:
        mach_was(name)
    
namen = ["Willi", "Heinz", "Karl"]   
#tu_was(12345) # - Knallt!
tu_was("HUHU") # - funktioniert, ist aber eher ungewollt
tu_was(namen)  # - funktioniert und ist von der Idee her gewollt