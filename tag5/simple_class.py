class SimpleClass:
    def mach_was(self):
        print("Mach was")

    def _hidden(self):
        print("Hidden") 

    def __totally_hidden(self):
        print("Double hidden")

o = SimpleClass()

o.mach_was() # Ok, offizelle Schnittstelle

# Das was nun folgt, geht zwar, ist aber echt keine schlaue Idee!
#o._hidden() # Funktioniert, ist aber keine gute Idee, da per Konvention private Methode
#o.__totally_hidden() # Funktioniert nicht, kann aber umgangen werden, siehe unten
#o._SimpleClass__totally_hidden() # Funktioniert, ist aber ganz schlechte Idee