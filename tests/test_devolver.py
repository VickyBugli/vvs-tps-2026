from biblioteca.gestor_biblioteca import GestorBiblioteca
from tests.stubs.stub_notificador import NotificadorStub
from biblioteca.libro import Libro, EstadoMaterial
from unittest.mock import MagicMock
import pytest

def test_devolver_exitoso():
    # ----- ARRANGE
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
    mock.reset_mock()

    # ----- ACT
    gestor.devolver('9781234567890')

    # ----- ASSERT
    assert libro.get_estado() == EstadoMaterial.DISPONIBLE
    mock.enviar.assert_called_once_with(
        destinatario='sistema',
        asunto='Devolución registrada',
        detalle='9781234567890'
    )