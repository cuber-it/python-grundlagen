class Tipp:
    def __init__(self):
        """
            Anlage eines Tipps
            :param tipp: Liste von 6 Zahlen
        """
        self._tipp = []

    def _verifizieren(self):
        """
            Überprüfung der Zahlen
        """
        # stelle sicher, dass es eine liste ist
        if isinstance(self._tipp, str):
            ValueError("Der Tipp muss eine Liste sein")
        # stelle sicher, dass die Zahlen in der Liste sind
        if isinstance(self._tipp, list):
            for zahl in self._tipp:
                if not isinstance(zahl, int):
                    raise ValueError("Die Zahlen müssen Integer sein")
        if len(self._tipp) != 6:
            raise ValueError("Ein Tipp besteht aus 6 Zahlen")
        for zahl in self._tipp:
            if zahl < 1 or zahl > 49:
                raise ValueError("Die Zahlen müssen zwischen 1 und 49 liegen")
        if len(set(self._tipp)) != 6:
            raise ValueError("Die Zahlen müssen eindeutig sein")

    def set_zahlen(self, zahlen):
        """
            Setzen der Zahlen
            :param zahlen: Liste von 6 Zahlen
        """
        self._tipp = zahlen
        self._verifizieren()

    def get_zahlen(self):
        """
            Ausgabe der Zahlen
            :return: Liste der Zahlen
        """
        return self._tipp

if __name__ == "__main__":
    # Pseudotests, besser als unittest anlegen
    tipp1 = Tipp([1, 2, 3, 4, 5, 6])
    #tipp2 = Tipp([1, 2, 3, 4, 5, 6, 7]) # ValueError
    #tipp3 = Tipp([1, 2, 3, 4, 5, 55]) # ValueError
    #tipp4 = Tipp([1, 2, 3, 4, 5, 5]) # ValueError
    #tipp5 = Tipp(["1", 2, 3, 4, 5, 6])
    #tipp6 = Tipp("1 2 3 4 5 6")