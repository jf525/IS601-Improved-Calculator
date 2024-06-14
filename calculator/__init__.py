from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def calculate(a, b, operation):
        '''Create and perform calculation, then return result of calculation'''
        calculation = Calculation(a, b, operation)
        return calculation.do_calculation()

    @staticmethod
    def add(a,b):
        return Calculator.calculate(a, b, add)
    
    @staticmethod
    def subtract(a,b):
        return Calculator.calculate(a, b, subtract)
    
    @staticmethod
    def multiply(a,b):
        return Calculator.calculate(a, b, multiply)
    
    @staticmethod
    def divide(a,b):
        return Calculator.calculate(a, b, divide)