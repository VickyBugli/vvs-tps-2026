from biblioteca.gestor_biblioteca import GestorBiblioteca
from tests.stubs.stub_notificador import NotificadorStub
from biblioteca.libro import Libro, EstadoMaterial
from unittest.mock import MagicMock
import pytest

def test_prestar_exitoso():
    # arrange
    stub = NotificadorStub()
    gestor = GestorBiblioteca(notificador=stub)
    libro = Libro(
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

def test_prestar_exitoso_mock():
    
    mock = MagicMock()                          
    gestor = GestorBiblioteca(notificador=mock)
    
    libro = Libro(
        isbn='9781234567890',
        titulo='Tinker Bell',
        autor='Disney',
        anio=1949,
        num_paginas=300
    )
    gestor.registrar(libro)

    gestor.prestar('9781234567890', '12345678', 7)

    assert libro.get_estado() == EstadoMaterial.PRESTADO

    mock.enviar.assert_called_once_with(
        destinatario='12345678',
        asunto='Préstamo confirmado',
        detalle=mock.enviar.call_args.kwargs['detalle']  # guarda lo del campo detalle
    )

def test_prestar_isbn_inexistente():
    # arrange 
    stub = NotificadorStub()
    gestor = GestorBiblioteca(notificador=stub)
        
    # verifico que se lance el error
    with pytest.raises(KeyError):
        gestor.prestar('9781234567890', '12345678', 7)
    # verifico que no hayan mensajes
    assert len(stub.envios) == 0 

def test_prestar_isbn_inexistente_mock():
    mock = MagicMock()
    gestor = GestorBiblioteca(notificador=mock)

    with pytest.raises(KeyError):
        gestor.prestar('9789999999999', '12345678', 7)

    # nunca se llamó a enviar() 
    mock.enviar.assert_not_called()

def prestar_libro_prestado():
    # arrange
    stub = NotificadorStub()
    gestor = GestorBiblioteca(notificador=stub)
    libro = Libro(
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

def test_prestar_libro_ya_prestado_mock():
    mock = MagicMock()
    gestor = GestorBiblioteca(notificador=mock)
    
    libro = Libro(
        isbn='9781234567890',
        titulo='Tinker Bell',
        autor='Disney',
        anio=1949,
        num_paginas=300
    )
    gestor.registrar(libro)
    
    # primer prestamo exitoso
    gestor.prestar('9781234567890', '12345678', 7)
    
    # reseteamos el mock para no contar el primer envío
    mock.reset_mock()

    with pytest.raises(PermissionError):
        gestor.prestar('9781234567890', '99999999', 7)

    # nunca se llamó a enviar() 
    mock.enviar.assert_not_called()