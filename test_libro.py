import pytest
from libro import Libro, EstadoMaterial


@pytest.fixture(scope="function")
def libro_valido():
    libro = Libro(
        isbn="1234567890",
        titulo="El diario de Anne Frank",
        autor="Anne Frank",
        anio=2003,
        num_paginas=220
    )
    return libro


def assert_invariante(libro):
    estado = libro.get_estado()
    lector = libro.get_lector()

    assert libro._isbn is not None and len(libro._isbn) >= 10
    assert libro._paginas > 0

    if estado in [EstadoMaterial.DISPONIBLE, EstadoMaterial.BAJA]:
        assert lector is None

    if estado in [EstadoMaterial.PRESTADO, EstadoMaterial.RESERVADO]:
        assert lector is not None


# ----------------------
# PRESTAR
# ----------------------

def test_prestar_dias_min(libro_valido):
    dni = "30123456"

    libro_valido.prestar(dni, 1)

    assert libro_valido.get_estado() == EstadoMaterial.PRESTADO
    assert libro_valido.get_lector() == dni
    assert_invariante(libro_valido)


def test_prestar_dias_max(libro_valido):
    dni = "30123456"

    libro_valido.prestar(dni, 30)

    assert libro_valido.get_estado() == EstadoMaterial.PRESTADO
    assert_invariante(libro_valido)


def test_prestar_dias_fuera_rango(libro_valido):
    estado_inicial = libro_valido.get_estado()
    lector_inicial = libro_valido.get_lector()

    with pytest.raises(ValueError):
        libro_valido.prestar("30123456", 31)

    assert libro_valido.get_estado() == estado_inicial
    assert libro_valido.get_lector() == lector_inicial
    assert_invariante(libro_valido)


def test_prestar_ya_prestado(libro_valido):
    libro_valido.prestar("30123456", 5)

    with pytest.raises(PermissionError):
        libro_valido.prestar("30999999", 5)

    assert libro_valido.get_estado() == EstadoMaterial.PRESTADO
    assert libro_valido.get_lector() == "30123456"
    assert_invariante(libro_valido)


def test_prioridad_estado_sobre_parametros(libro_valido):
    libro_valido.prestar("30123456", 5)

    with pytest.raises(PermissionError):
        libro_valido.prestar("", -1)


# ----------------------
# DEVOLVER
# ----------------------

def test_devolver_ok(libro_valido):
    libro_valido.prestar("30123456", 5)

    libro_valido.devolver()

    assert libro_valido.get_estado() == EstadoMaterial.DISPONIBLE
    assert libro_valido.get_lector() is None
    assert_invariante(libro_valido)


def test_devolver_invalido(libro_valido):
    estado_inicial = libro_valido.get_estado()
    lector_inicial = libro_valido.get_lector()

    with pytest.raises(PermissionError):
        libro_valido.devolver()

    assert libro_valido.get_estado() == estado_inicial
    assert libro_valido.get_lector() == lector_inicial
    assert_invariante(libro_valido)


# ----------------------
# RESERVAR
# ----------------------

def test_reservar_ok(libro_valido):
    dni = "30123456"

    libro_valido.reservar(dni)

    assert libro_valido.get_estado() == EstadoMaterial.RESERVADO
    assert libro_valido.get_lector() == dni
    assert_invariante(libro_valido)


# ----------------------
# BAJA
# ----------------------

def test_baja_prestado(libro_valido):
    libro_valido.prestar("30123456", 5)

    with pytest.raises(PermissionError):
        libro_valido.dar_de_baja()

    assert libro_valido.get_estado() == EstadoMaterial.PRESTADO
    assert_invariante(libro_valido)

# --------------- agregado ----------------
def test_reservar_estado_invalido(libro_valido):
    libro_valido.prestar("30123456", 5)

    with pytest.raises(PermissionError):
        libro_valido.reservar("123")
