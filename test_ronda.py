import pytest
from jugador import Jugador
from ronda import Ronda

def test_prueba():
    assert True

def test_constructor():
    ronda = Ronda()
    assert ronda.jugadores == []

def test_str():
    ronda = Ronda()
    jugador1 = Jugador("Tomas")
    jugador2 = Jugador("Juan")
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    msj = str(ronda)
    assert "Tomas" in msj
    assert "Juan" in msj
    assert "fichas" in msj

def test_agregarJugador():
    ronda = Ronda()
    jugador = Jugador("Tomas")
    ronda.agregarJugador(jugador)
    assert jugador in ronda.jugadores

def test_agregarJugador_error():
    ronda = Ronda()
    jugador = Jugador("Tomas")
    jugador.sacarFicha(5)
    with pytest.raises(ValueError):
        ronda.agregarJugador(jugador)

def test_sacarJugadoresSinFichas():
    ronda = Ronda()
    jugador1 = Jugador("Tomas")
    jugador2 = Jugador("Juan")
    jugador3 = Jugador("Pedro")
    jugador3.sacarFicha(5)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    ronda.agregarJugador(jugador3)
    ronda.sacarJugadoresSinFichas()
    assert jugador3 not in ronda.jugadores

def test_jugadorEnTurno():
    ronda = Ronda()
    jugador1 = Jugador("Tomas")
    jugador2 = Jugador("Juan")
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    assert ronda.jugadorEnTurno() == jugador1

def test_pasarTurno():
    ronda = Ronda()
    jugador1 = Jugador("Tomas")
    jugador2 = Jugador("Juan")
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    ronda.pasarTurno()
    assert ronda.jugadorEnTurno() == jugador2

def test_quedaUnSoloJugador():
    ronda = Ronda()
    jugador1 = Jugador("Tomas")
    ronda.agregarJugador(jugador1)
    assert ronda.quedaUnSoloJugador()
    jugador2 = Jugador("Juan")
    ronda.agregarJugador(jugador2)
    assert not ronda.quedaUnSoloJugador()