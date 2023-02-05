from main import willans
from pytest import raises

def test_0Throws():
    with raises(ZeroDivisionError):
       willans(0)

def test_1stPrimeIs2():
    assert willans(1) == 2

def test_2ndPrimeIs3():
    assert willans(2) == 3

def test_3rdPrimeIs5():
    assert willans(3) == 5

def test_4thPrimeIs7():
    assert willans(4) == 7

def test_5thPrimeIs11():
    assert willans(5) == 11

def test_6thPrimeIs13():
    assert willans(6) == 13

def test_7thPrimeIs17():
    assert willans(7) == 17

def test_8thPrimeIs19():
    assert willans(8) == 19

def test_9thPrimeIs23():
    assert willans(9) == 23

def test_10thPrimeIs29():
    assert willans(10) == 29