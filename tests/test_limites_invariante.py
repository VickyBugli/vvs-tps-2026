import pytest
from libro import Libro, EstadoMaterial


def crear_libro():
    return Libro("1234567890", "Titulo", "Autor", 2020, 100)


class TestLimitesInvariante:

    # ----------------------
    # ISBN
    # ----------------------

    def test_isbn_limite_valido(self):
        libro = crear_libro()
        libro.prestar("30123456", 15)
        assert libro.get_estado() == EstadoMaterial.PRESTADO

    def test_isbn_invalido(self):
        with pytest.raises(ValueError):
            Libro("123456789", "Titulo", "Autor", 2020, 100)

    # ----------------------
    # PÁGINAS
    # ----------------------

    def test_paginas_limite_valido(self):
        libro = Libro("1234567890", "Titulo", "Autor", 2020, 1)
        libro.prestar("30123456", 15)
        assert libro.get_estado() == EstadoMaterial.PRESTADO

    def test_paginas_invalido(self):
        with pytest.raises(ValueError):
            Libro("1234567890", "Titulo", "Autor", 2020, 0)

    # ----------------------
    # ESTADO + CONSISTENCIA
    # ----------------------

    def test_transicion_valida(self):
        libro = crear_libro()
        libro.prestar("30123456", 15)

        assert libro.get_estado() == EstadoMaterial.PRESTADO
        assert libro.get_lector() == "30123456"

    def test_prestar_libro_ya_prestado(self):
        libro = crear_libro()
        libro.prestar("99999999", 5)

        with pytest.raises(PermissionError):
            libro.prestar("30123456", 15)

    def test_prestar_libro_baja(self):
        libro = crear_libro()
        libro.dar_de_baja()

        with pytest.raises(PermissionError):
            libro.prestar("30123456", 15)
    
    