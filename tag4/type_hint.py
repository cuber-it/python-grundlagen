from typing import List, Dict, Optional

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> List[int, str]:
    return a + b, "Ergebnis"

def get_items() -> List[str]:
    return ["apple", "banana", "cherry"]

def get_user_data(user_id: int) -> Dict[str, str]:
    return {"id": str(user_id), "name": "Alice"}

def optional_example(value: Optional[int] = None) -> str:
    return f"Value is {value}" if value is not None else "No value provided"

# Example usage
print(greet("Alice"))
print(add_numbers(5, 10))
print(get_items())
print(get_user_data(42))
print(optional_example())
print(optional_example(100))
