import pytest
from jugador import Jugador

def test_prueba():
    assert True

def test_constructor():
    jugador = Jugador("Tomas")
    assert jugador.fichas == 5

def test_str():
    jugador = Jugador("Tomas")
    msj = str(jugador)
    assert "Tomas" in msj
    assert "fichas" in msj
    assert "5" in msj

def test_darFicha():
    jugador = Jugador("Tomas")
    jugador.darFicha(3)
    assert jugador.fichas == 8

    jugador = Jugador("Tomas")
    jugador.darFicha(5)
    assert jugador.fichas == 10

def test_sacarFicha():
    jugador = Jugador("Tomas")
    jugador.sacarFicha(3)
    assert jugador.fichas == 2

    jugador = Jugador("Tomas")
    jugador.sacarFicha(5)
    assert jugador.fichas == 0

def test_sacarFicha_error():
    jugador = Jugador("Tomas")
    with pytest.raises(ValueError):
        jugador.sacarFicha(6)

def test_tieneFicha():
    jugador = Jugador("Tomas")
    assert jugador.tieneFicha()
    jugador.sacarFicha(4)
    assert jugador.tieneFicha(1)
    assert not jugador.tieneFicha(5)

def test_sinFichas():
    jugador = Jugador("Tomas")
    assert not jugador.sinFichas()
    jugador.sacarFicha(5)
    assert jugador.sinFichas()