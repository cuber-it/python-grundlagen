def add(a: int, b: int) -> int:
    return a + b

def get_items() -> list[str]:
    return ["a", "b"]

def config(options: dict[str, int]) -> None:
    for key, value in options.items():
        print(f"{key}: {value}")

def main() -> None:
    print("Hello, World!")
    print(add("Hello", 2)) # TypeError: unsupported operand type(s) for +: 'str' and 'int'
    print(get_items())
    config({"a": 1, "b": 2})

if __name__ == "__main__": # __main__ block
    # __name__ ist der Name des Moduls, das gerade ausgeführt wird
    # Wenn das Modul direkt ausgeführt wird, ist __name__ gleich "__main__"
    # Wenn das Modul importiert wird, ist __name__ gleich dem Namen des Moduls
    # __name__ == "__main__" ist eine Möglichkeit, um zu überprüfen, ob das Modul direkt ausgeführt wird
    # und nicht importiert wurde
    # Wenn das Modul direkt ausgeführt wird, wird die Funktion main() aufgerufen
    # Wenn das Modul importiert wird, wird die Funktion main() nicht aufgerufen
    # Das ist nützlich, um zu verhindern, dass Code ausgeführt wird, wenn das Modul importiert wird
    main()