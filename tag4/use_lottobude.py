import lottobude as lb # lottobude ist mir zu lang, ich nehme einen alias "lb"

anzahl = int(input("Wie oft wollen Sie spielen? "))

for _ in range(anzahl):
    lb.lotto_bude()

print("Das war's für heute. Viel Glück beim nächsten Mal!")