class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod
    def create(a, b, operation):
        return  Calculation(a, b, operation)

    def do_calculation(self):
        return self.operation(self.a, self.b)