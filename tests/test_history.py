'''My Calculator Test'''

from calculator.calculation import Calculation
from calculator.history import History

#only importing add and subtract for testing
from calculator.operations import add, subtract

def setup_test_calculations():
    '''Clear current history and and add sample calculations for testing'''
    History.clear_history()
    History.add_history(Calculation(10, 4, add))
    History.add_history(Calculation(20, 12, subtract))

def test_add_history():
    '''Testing adding a calculation to history.'''
    setup_test_calculations()
    calc = Calculation(2, 2, add)
    History.add_history(calc)
    assert History.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history():
    '''Test retrieving the entire calculation history.'''
    setup_test_calculations()
    history = History.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history():
    '''Test clearing the entire calculation history.'''
    setup_test_calculations()
    History.clear_history()
    assert len(History.get_history()) == 0, "History was not cleared"

def test_get_latest():
    '''Test getting the latest calculation from the history.'''
    setup_test_calculations()
    latest = History.get_latest()
    assert latest.a == 20 and latest.b == 12, "Did not get the correct latest calculation"

def test_get_latest_with_empty_history():
    '''Test getting the latest calculation when the history is empty.'''
    setup_test_calculations()
    History.clear_history()
    assert History.get_latest() is None, "Expected None for latest calculation with empty history"
