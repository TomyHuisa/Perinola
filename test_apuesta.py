import pytest
from apuesta import Apuesta
def test_prueba():
    assert(True)

def test_constructor():
    a = Apuesta()
    assert(a.fichas == 0)

def test_repr():
    a=Apuesta()
    msj = a.__repr__()
    assert("Apuesta:" in msj)
    assert("fichas" in msj)
    assert("4" in msj)

def test_ponerFicha():
    a = Apuesta()
    a.ponerFicha(1)
    assert(a.fichas == 1)

    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2)

def test_tomarFicha_sin_argumentos():
    a= Apuesta()
    a.ponerFicha(2)
    a.ponerFicha(3)
    assert(a.fichas == 5)

def test_tomarFicha_sin_argumentos():
    a = Apuesta()
    a.fichas = 5 
    a.tomarFicha()
    assert(a.fichas == 4)
def test_tomarFicha_error():
    with pytest.raises(ValueError):
        a = Apuesta()
        a.fichas = 5
        a.tomarFicha(6)