import pytest
from libro import Libro, EstadoMaterial


def crear_libro():
    return Libro("1234567890", "Titulo", "Autor", 2020, 100)


class TestParticionCategoria:

    # ----------------------
    # CASOS VÁLIDOS
    # ----------------------

    def test_prestar_limite_inferior(self):
        libro = crear_libro()
        libro.prestar("30123456", 1)
        assert libro.get_estado() == EstadoMaterial.PRESTADO

    def test_prestar_caso_tipico(self):
        libro = crear_libro()
        libro.prestar("30123456", 15)
        assert libro.get_estado() == EstadoMaterial.PRESTADO

    def test_prestar_limite_superior(self):
        libro = crear_libro()
        libro.prestar("30123456", 30)
        assert libro.get_estado() == EstadoMaterial.PRESTADO

    # ----------------------
    # ERRORES EN DÍAS
    # ----------------------

    @pytest.mark.parametrize("dias", [0, -1, 31])
    def test_error_dias_invalidos(self, dias):
        libro = crear_libro()
        with pytest.raises(ValueError):
            libro.prestar("30123456", dias)

    # ----------------------
    # ERRORES EN DNI
    # ----------------------

    @pytest.mark.parametrize("dni", ["", "123", None])
    def test_error_dni_invalido(self, dni):
        libro = crear_libro()
        with pytest.raises(ValueError):
            libro.prestar(dni, 15)

    # ----------------------
    # ERRORES DE ESTADO
    # ----------------------

    def test_error_estado_prestado(self):
        libro = crear_libro()
        libro.prestar("99999999", 5)

        with pytest.raises(PermissionError):
            libro.prestar("30123456", 15)

    def test_error_estado_baja(self):
        libro = crear_libro()
        libro.dar_de_baja()

        with pytest.raises(PermissionError):
            libro.prestar("30123456", 15)

    