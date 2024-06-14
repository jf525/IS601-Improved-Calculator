from typing import List
from calculator.calculation import Calculation

class History:
    history: List[Calculation] = []

    @classmethod
    def add_history(cls, calculation: Calculation):
        '''Add a new calculation to the calculator's history'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Get calculation history'''
        #if (cls.history.__len__ <= 0)
            #return "No history available"
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Clear calculation history'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''Get last calculation in history'''
        if cls.history:
            return cls.history[-1]
        return None