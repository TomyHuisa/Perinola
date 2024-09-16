import pytest
from perinola import Perinola

def test_prueba():
    assert True

def test_constructor():
    perinola = Perinola()
    assert perinola.cara_visible in Perinola.caras

def test_repr():
    perinola = Perinola()
    msj = repr(perinola)
    assert "Salio:" in msj
    assert str(perinola.cara_visible) in msj

def test_tirar():
    perinola = Perinola()
    caras = ("Pon 1", "Toma 2", "Todos Ponen", "Toma 1", "Pon2", "Toma Todo")
    resultado = perinola.tirar()
    assert resultado in caras

def test_tirar_varias_veces():
    perinola = Perinola()
    resultados = [perinola.tirar() for _ in range(10)]
    assert all(resultado in ("Pon 1", "Toma 2", "Todos Ponen", "Toma 1", "Pon2", "Toma Todo") for resultado in resultados)

def test_tirar_no_repite():
    perinola = Perinola()
    resultados = [perinola.tirar() for _ in range(6)]
    assert len(set(resultados)) > 1
