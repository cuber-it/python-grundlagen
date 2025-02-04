# Aufgabe
#
# Berechnung des BMI und Auswertung
#
# BMI = Gewicht / (Größe * Größe)
#
# Auswertung:
# - BMI < 18,5: Untergewicht
# - BMI 18,5 - 24,9: Normalgewicht
# - BMI 25 - 29,9: Übergewicht
# - BMI > 30: Adipositas
#   
# Der Benutzer soll sein Gewicht und seine Größe eingeben
# Das Programm berechnet den BMI und gibt die Auswertung aus

print("BMI Calculator")
print("="*40)

try:
    groesse = float(input("Bitte geben Sie Ihre Größe in Metern ein: ").replace(",", ".")) # 1,80 -> 1.80
    gewicht = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm ein: ").replace(",", ".")) # 80,5 -> 80.5   
    bmi = gewicht / (groesse * groesse)

    if bmi < 18.5:
        print(f"Untergewicht {bmi:.2f}")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"Normalgewicht {bmi:.2f}")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"Übergewicht {bmi:.2f}")
    else:
        print(f"Adipositas {bmi:.2f}")
except ValueError:
    print("Fehler: Bitte geben Sie eine Zahl ein.")
except ZeroDivisionError:
    print("Fehler: Division durch Null")    

print("Programmende")      
