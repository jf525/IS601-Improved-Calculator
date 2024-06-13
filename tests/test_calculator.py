'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Testing that the addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Testing that the subtaction function works'''
    assert subtract(2,2) == 0
    