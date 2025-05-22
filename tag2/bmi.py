gewicht = input("Gib dein Gewicht in kg an: ").replace(",",".")
groesse = input("Gib deine Größe in cm an: ").replace(",",".")
# BMI = Gewicht in kg / (Größe in m)²
gewicht = float(gewicht)
groesse = float(groesse)
groesse = groesse / 100
bmi = gewicht / (groesse ** 2)
print("Dein BMI ist: " + str(bmi))
if bmi < 18.5:
    print("Du bist untergewichtig.")
elif 18.5 <= bmi < 25:
    print("Du hast Normalgewicht.")
elif 25 <= bmi < 30:
    print("Du bist übergewichtig.")
elif 30 <= bmi < 35:
    print("Du hast Adipositas Grad 1.")
elif 35 <= bmi < 40:
    print("Du hast Adipositas Grad 2.")
elif bmi >= 40:
    print("Du hast Adipositas Grad 3.")
else:
    print("Ungültige Eingabe.")