'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Testing that the addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Testing that the subtaction function works'''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Testing that the multiplication function works'''
    assert multiply(2,3) == 6

def test_division():
    '''Testing that the division function works'''
    assert divide(8,2) == 4
    