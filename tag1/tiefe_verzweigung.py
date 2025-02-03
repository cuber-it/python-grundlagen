def check_values(a, b, c, d):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    print("Alle Werte sind positiv!")
                else:
                    print("Fehler: d ist nicht positiv.")
            else:
                print("Fehler: c ist nicht positiv.")
        else:
            print("Fehler: b ist nicht positiv.")
    else:
        print("Fehler: a ist nicht positiv.")

# Testfälle
check_values(1, 2, 3, -4)

# Besser: z.B. guard clauses
def check_values(a, b, c, d):
    if a <= 0:
        print("Fehler: a ist nicht positiv.")
        return
    if b <= 0:
        print("Fehler: b ist nicht positiv.")
        return
    if c <= 0:
        print("Fehler: c ist nicht positiv.")
        return
    if d <= 0:
        print("Fehler: d ist nicht positiv.")
        return

    print("Alle Werte sind positiv!")

# Testfälle
check_values(1, 2, 3, -4)
