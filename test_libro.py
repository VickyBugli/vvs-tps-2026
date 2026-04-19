import pytest
from libro import Libro, EstadoMaterial

@pytest.fixture(scope="function")
def libro_valido():
    # Arrange: estado inicial válido
    libro = Libro(
        isbn="1234567890",
        titulo="El diario de Anne Frank",
        autor="Anne Frank",
        anio=2003,
        num_paginas=220
    )
    # Por constructor ya queda en estado DISPONIBLE y sin lector
    return libro

def assert_invariante(libro):
    estado = libro.get_estado()
    lector = libro.get_lector()

    assert libro._isbn is not None and len(libro._isbn) >= 10
    assert libro._paginas > 0

    if estado.name in ["disponible", "baja"]:
        assert lector is None
    if estado.name in ["prestado", "reservado"]:
        assert lector is not None

def test_prestar_dias_min(libro_valido):
    # Arrange
    dni = "123"

    # Act
    libro_valido.prestar(dni, 1)

    # Assert
    assert libro_valido.get_estado().name == "prestado"
    assert libro_valido.get_lector() == dni
    assert_invariante(libro_valido)

def test_prestar_dias_max(libro_valido):
    # Arrange
    dni = "123"

    # Act
    libro_valido.prestar(dni, 30)

    # Assert
    assert libro_valido.get_estado().name == "prestado"
    assert_invariante(libro_valido)

def test_prestar_dias_fuera_rango(libro_valido):
    # Arrange
    estado_inicial = libro_valido.get_estado()
    lector_inicial = libro_valido.get_lector()

    # Act + Assert
    with pytest.raises(ValueError):
        libro_valido.prestar("123", 31)

    # Assert completo
    assert libro_valido.get_estado() == estado_inicial
    assert libro_valido.get_lector() == lector_inicial
    assert_invariante(libro_valido)

def test_prestar_ya_prestado(libro_valido):
    # Arrange
    libro_valido.prestar("123", 5)

    # Act y Assert
    with pytest.raises(PermissionError):
        libro_valido.prestar("456", 5)

    assert libro_valido.get_estado().name == "prestado"
    assert libro_valido.get_lector() == "123"
    assert_invariante(libro_valido)

def test_devolver_ok(libro_valido):
    # Arrange
    libro_valido.prestar("123", 5)

    # Act
    libro_valido.devolver()

    # Assert
    assert libro_valido.get_estado().name == "disponible"
    assert libro_valido.get_lector() is None
    assert_invariante(libro_valido)

def test_devolver_invalido(libro_valido):
    # Arrange
    estado_inicial = libro_valido.get_estado()
    lector_inicial = libro_valido.get_lector()

    # Act + Assert
    with pytest.raises(PermissionError):
        libro_valido.devolver()

    # Assert
    assert libro_valido.get_estado() == estado_inicial
    assert libro_valido.get_lector() == lector_inicial
    assert_invariante(libro_valido)

def test_reservar_ok(libro_valido):
    # Arrange
    dni = "123"

    # Act
    libro_valido.reservar(dni)

    # Assert
    assert libro_valido.get_estado().name == "reservado"
    assert libro_valido.get_lector() == dni
    assert_invariante(libro_valido)

def test_baja_prestado(libro_valido):
    # Arrange
    libro_valido.prestar("123", 5)
    estado_inicial = libro_valido.get_estado()
    lector_inicial = libro_valido.get_lector()

    # Act + Assert
    with pytest.raises(PermissionError):
        libro_valido.dar_de_baja()

    # Assert
    assert libro_valido.get_estado() == estado_inicial
    assert libro_valido.get_lector() == lector_inicial
    assert_invariante(libro_valido)

def test_reservar_ok(libro_valido):
    # Arrange
    dni = "123"

    # Act
    libro_valido.reservar(dni)

    # Assert
    assert libro_valido.get_estado().name == "reservado"
    assert libro_valido.get_lector() == dni
    assert_invariante(libro_valido)

def test_baja_prestado(libro_valido):
    # Arrange
    libro_valido.prestar("123", 5)

    # Act y Assert
    with pytest.raises(PermissionError):
        libro_valido.dar_de_baja()

    assert libro_valido.get_estado().name == "prestado"
    assert_invariante(libro_valido)