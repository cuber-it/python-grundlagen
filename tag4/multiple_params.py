def sum(*args): # *args entspricht einer Liste
    result = 0
    for value in args:
        result += value
    return result

def mutli_params(**kwargs): # **kwargs entspricht einem Dictionary
    if "name" in kwargs:
        print("Name:", kwargs["name"])
    if "age" in kwargs:
        print("Age:", kwargs["age"])
    if "city" in kwargs:
        print("City:", kwargs["city"])
    if "country" in kwargs:
        print("Country:", kwargs["country"])
    if "values" in kwargs:
        print("Summe:", sum(*kwargs["values"]))

mutli_params(name="Willi", age=42, city="Berlin", country="Germany", values=[1, 2, 3, 4, 5])
mutli_params(name="Willi", age=42, city="Berlin", country="Germany")
mutli_params(name="Willi", age=42, city="Berlin")
mutli_params(name="Willi", age=42)
mutli_params(name="Willi")
# - mutli_params(1234) # Fehler: Funktion erwartet named parameters
