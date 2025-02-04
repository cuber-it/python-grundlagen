#!/usr/bin/env python3

def benutzerabfrage():
    groesse = float(input("Bitte geben Sie Ihre Größe in Metern ein: ").replace(",", ".")) # 1,80 -> 1.80
    gewicht = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm ein: ").replace(",", ".")) # 80,5 -> 80.5   

    return groesse, gewicht

def berechne_bmi(groesse, gewicht):
    bmi = gewicht / (groesse * groesse)

    return bmi

def auswertung_bmi(bmi):
    if bmi < 18.5:
        print(f"Untergewicht {bmi:.2f}")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"Normalgewicht {bmi:.2f}")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"Übergewicht {bmi:.2f}")
    else:
        print(f"Adipositas {bmi:.2f}")

 


print("BMI Calculator")
print("="*40)

try:
    groesse, gewicht = benutzerabfrage()

    bmi = berechne_bmi(groesse, gewicht)

    auswertung_bmi(bmi)
except ValueError:
    print("Fehler: Bitte geben Sie eine Zahl ein.")
except ZeroDivisionError:
    print("Fehler: Division durch Null")    

print("Programmende")     
