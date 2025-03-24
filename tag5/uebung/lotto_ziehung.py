import random

class Ziehung:
    def __init__(self):
        self._zahlen = []

    def ziehen(self):
        self._zahlen = random.sample(range(1, 50), 6)
        return self._zahlen

    def get_zahlen(self):
        return self._zahlen
    
if __name__ == "__main__":
    ziehung = Ziehung()
    print(ziehung.ziehen()) # [ sechs zahlen ]
    print(ziehung.get_zahlen()) # [ die gleichen sechs zahlen ]