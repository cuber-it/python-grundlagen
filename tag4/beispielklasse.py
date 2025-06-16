class Calc:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b

    def sub(self, a, b):
        self.result = a - b

    def mul(self, a, b):
        self.result = a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result = a / b

    def get_result(self):
        return self.result
    
    def reset(self):
        self.result = 0


calc_1 = Calc()
calc_2 = Calc()

calc_1.add(5, 3)
print(calc_1.get_result())  # Output: 8
calc_2.mul(4, 2)
print(calc_2.get_result())  # Output: 8
calc_1.sub(10, 4)
print(calc_1.get_result())  # Output: 6
calc_2.div(8, 2)
print(calc_2.get_result())  # Output: 4.0
calc_1.reset()
print(calc_1.get_result())  # Output: 0
    
