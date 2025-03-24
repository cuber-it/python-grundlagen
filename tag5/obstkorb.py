class FruchtKorb:
    def __init__(self, einlage = 'Papier'):
        self._inhalt = {} # Leerer Obstkorb
        self._einlage = einlage
    
    def hineinlegen(self, frucht, farbe):
        self._inhalt[frucht] = farbe
        
    def herausholen(self, frucht):
        return self._inhalt.get(frucht, 'nicht im Korb')
        
    def inhalt(self):
        for frucht, farbe in self._inhalt.items():
            print(frucht, farbe)
    
    def get_einlage(self):
        return self._einlage
        
    def set_einlage(self, einlage_art):
        self._einlage = einlage_art
            
korb_1 = FruchtKorb()
korb_1.hineinlegen('apple', 'green')
korb_1.hineinlegen('banana', 'green')

korb_2 = FruchtKorb('Tuch')
korb_2.hineinlegen('orange', 'orange')

print("korb_1:", korb_1.herausholen('orange'))
print("korb_1:", korb_1.get_einlage())
print("Korb_1-Inhalte:")
korb_1.inhalt()

korb_1.hineinlegen('orange', korb_2.herausholen('orange'))
korb_1.inhalt()
korb_1.set_einlage('Stroh')
print("korb_1:", korb_1.get_einlage())

print("korb_2:", korb_2.herausholen('orange'))
print("korb_2:", korb_2.get_einlage())