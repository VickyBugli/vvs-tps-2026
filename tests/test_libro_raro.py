import pytest
from biblioteca.libro_raro import LibroRaro
from biblioteca.libro import EstadoMaterial
from tests.stubs.stub_notificador import NotificadorStub
from biblioteca.gestor_biblioteca import GestorBiblioteca


def libro_raro():
    return LibroRaro(
        isbn='9781234567890',
        titulo='Edición única',
        autor='Autor',
        anio=1949,
        num_paginas=300
    )

def test_prestar_exitoso():
    # arrange
    stub = NotificadorStub()
    gestor = GestorBiblioteca(notificador=stub)
    libro = LibroRaro(
        isbn='9781234567890',
        titulo='Tinker Bell',
        autor='Disney',
        anio=1949,
        num_paginas=300
    )
    gestor.registrar(libro)

    # act
    gestor.prestar('9781234567890', '12345678', 7)

    # assert
    # verificar estado
    assert libro.get_estado() == EstadoMaterial.PRESTADO
    # verificar asunto correcto
    assert stub.envios[0]['asunto'] == 'Préstamo confirmado'

def prestar_libro_prestado():
    # arrange
    stub = NotificadorStub()
    gestor = GestorBiblioteca(notificador=stub)
    libro = LibroRaro(
        isbn='9781234567890',
        titulo='Tinker Bell',
        autor='Disney',
        anio=1949,
        num_paginas=300
    )
    gestor.registrar(libro)

    # act
    gestor.prestar('9781234567890', '12345678', 7)
    
    # borramos el libro
    stub.envios.clear()

    # verifico el error arrojado
    with pytest.raises(PermissionError):
        gestor.prestar('9781234567890', '12345678', 7)

    # verifico que no hayan mensajes
    assert len(stub.envios) == 0


def test_prestar_hasta_7_dias():
    l = libro_raro()
    l.prestar('12345678', 7)
    assert l.get_estado() == EstadoMaterial.PRESTADO

def test_prestar_mas_de_7_dias():
    l = libro_raro()
    with pytest.raises(ValueError):
        l.prestar('12345678', 8)

def test_reservar_prohibida():
    l = libro_raro()
    with pytest.raises(PermissionError):
        l.reservar('12345678')