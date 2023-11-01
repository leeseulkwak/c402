class Calculator:
    entries=[]

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Division by zero is not allowed"
        return a / b

    @classmethod
    def add_entry(cls, a, b, operation, result):
        entry = f"{a} {operation} {b} = {result}"
        cls.entries.append(entry)

    @classmethod
    def display(cls):
        for entry in cls.entries:
            print(entry)
