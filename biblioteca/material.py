# biblioteca/material.py

from biblioteca.libro import EstadoMaterial


class Material:
    def __init__(self, titulo: str, autor: str, anio: int):
        if anio <= 1900:
            raise ValueError('El año debe ser posterior a 1900')
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._estado = EstadoMaterial.DISPONIBLE

    def prestar(self, dni_lector: str, dias: int) -> str:
        raise NotImplementedError

    def devolver(self) -> None:
        raise NotImplementedError

    def get_estado(self) -> EstadoMaterial:
        return self._estado