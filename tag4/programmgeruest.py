#!/usr/bin/env python

import sys
# ...

def mach_was():
    print("Mach was")
# ...

def main():
    mach_was()
    print("Hallo Welt")

if __name__ == '__main__': # Prüft, ob das Modul direkt aufgerufen wird = standalone oder als import
    main() # Aufruf der main-Funktion bei direktem Aufruf