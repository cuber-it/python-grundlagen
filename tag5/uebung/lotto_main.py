import lotto_tipp
import lotto_ziehung

class Lotto:
    def __init__(self):
        self._tipp = lotto_tipp.Tipp()
        self._lostrommel = lotto_ziehung.Ziehung()
        self._treffer = []
        self._gewinnklasse = 0  

    def set_tipp(self, tipp):
        self._tipp.set_zahlen(tipp)

    def get_tipp(self):
        return self._tipp.get_zahlen()
    
    def ziehen(self):
        self._lostrommel.ziehen()
        ziehung = self._lostrommel.get_zahlen()
        self._gewinnklasse = self._vergleichen(ziehung)
        return ziehung
    
    def get_ziehung(self):
        return self._lostrommel.get_zahlen()   
    
    def get_gewinnklasse(self):
        return self._gewinnklasse

    def get_treffer(self):
        return self._treffer
    
    def _vergleichen(self, ziehung):
        tipp = self.get_tipp()
        ziehung = self.get_ziehung()
        treffer = list(set(tipp).intersection(set(ziehung)))
        self._treffer = treffer
        if len(treffer) == 6:
            return 1
        elif len(treffer) == 5:
            return 2
        elif len(treffer) == 4:
            return 3
        elif len(treffer) == 3:
            return 4
        else:
            return 0
        
if __name__ == "__main__":
    lottobude = Lotto()
    lottobude.set_tipp([1, 2, 3, 4, 5, 6])
    print("Ihr Tipp", lottobude.get_tipp())
    lottobude.ziehen()
    print("Ziehung", lottobude.get_ziehung())
    print("Gewinnklasse", lottobude.get_gewinnklasse())
    print("Treffer", lottobude.get_treffer())

