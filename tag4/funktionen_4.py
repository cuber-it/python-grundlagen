# Named PArameters, Beispiele dafür

def addiere(a, b):
    return a + b

print(addiere(1,2))
print(addiere(a=1, b=2))
print(addiere(b=2, a=1))

def read_file(file_name, encoding="utf-8"):
    with open(file_name, 'r', encoding=encoding) as file:
        content = file.read()
    return content

print(read_file("test.txt"))
print(read_file("test.txt", "iso-8859-1"))
print(read_file("test.txt", encoding="iso-8859-1"))
print(read_file(file_name="test.txt", encoding="iso-8859-1"))
print(read_file(file_name="test.txt"))
print(read_file("test.txt", encoding="utf-8"))
print(read_file(encoding="utf-8", file_name="test.txt"))

def berechnung(a, b, c=1, d=10): # DEfaultwerte 1 und 10
    return (a + b) * c / d

print(berechnung(1, 2))
print(berechnung(1, 2, 3)) # c -> 3, d bleibt 10
print(berechnung(1, 2, 3, 4)) # c -> 3, d -> 4
print(berechnung(1, 2, d=4)) # c bleibt 1, d -> 4
print(berechnung(1, 2, c=3)) # c -> 3, d bleibt 10
print(berechnung(1, 2, d=4, c=3)) # c -> 3, d -> 4
print(berechnung(d=4, a=1, c=3, b=2)) # a->1, b->2, c -> 3, d -> 4