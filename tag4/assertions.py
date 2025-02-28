def mach_was(name):
    assert type(name) == str, "Name muss ein String sein"
    print("Hello", name)
    return 0
    
def tu_was(namen): # namen ist lokale Variable und Parameter
    assert type(namen) == list, "Namen muss eine Liste sein"
    counter = 0 # lokale Variable
    for name in namen: # name ist eine lokale Variable
        try:
            mach_was(name)
            counter += 1
        except AssertionError as e:
            print("Fehler:", e)
    return counter
    
namen = ["Willi", "Heinz", "Karl"]   # globale Variable
# evtl. PRüfung das es wirklich Liste von sTrings ist und dann auf die Assertions verzichten
ausgegeben = tu_was(namen)
print("Anzahl der ausgegebenen Namen:", ausgegeben)