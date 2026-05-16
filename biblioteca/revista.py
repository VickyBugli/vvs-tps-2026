# biblioteca/revista.py

from biblioteca.material import Material
from biblioteca.libro import EstadoMaterial


class Revista(Material):
    def __init__(self, numero_edicion: int, periodicidad: str,
                 titulo: str, autor: str, anio: int):
        super().__init__(titulo, autor, anio)  # ← valida el año
        self._numero_edicion = numero_edicion
        self._periodicidad = periodicidad

    def prestar(self, dni_lector: str, dias: int) -> str:
        if self._estado != EstadoMaterial.DISPONIBLE:
            raise IllegalStateException("No disponible")
        if dias < 1 or dias > 7:
            raise ValueError("Revistas: máx 7 días")
        self._estado = EstadoMaterial.PRESTADO
        return f'Revista prestada por {dias} días'

    def devolver(self) -> None:
        if self._estado != EstadoMaterial.PRESTADO:
            raise PermissionError("No está prestada")
        self._estado = EstadoMaterial.DISPONIBLE