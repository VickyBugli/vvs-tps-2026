# biblioteca/libro.py
from enum import Enum


class EstadoMaterial(Enum):
    DISPONIBLE = 'disponible'
    PRESTADO   = 'prestado'
    RESERVADO  = 'reservado'
    BAJA       = 'baja'


class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str,
                 anio: int, num_paginas: int):
        if not isbn or len(isbn) < 10:
            raise ValueError('ISBN inválido')
        if num_paginas <= 0:
            raise ValueError('num_paginas debe ser positivo')
        self._isbn       = isbn
        self._titulo     = titulo
        self._autor      = autor
        self._anio       = anio
        self._paginas    = num_paginas
        self._estado     = EstadoMaterial.DISPONIBLE
        self._lector_dni = None


 def prestar(self, dni, dias):
    if dias < 1 or dias > 30:
        raise ValueError("Días inválidos")

    if self._estado != EstadoMaterial.DISPONIBLE:
        raise PermissionError("No disponible")

    self._estado = EstadoMaterial.PRESTADO
    self._lector = dni


def devolver(self):
    if self._estado != EstadoMaterial.PRESTADO:
        raise PermissionError("No se puede devolver si no está prestado")

    self._estado = EstadoMaterial.DISPONIBLE
    self._lector = None


    def reservar(self, dni_lector: str) -> None:
        """Reserva el libro. Pre: estado=DISPONIBLE."""
        if self._estado != EstadoMaterial.DISPONIBLE:
            raise PermissionError('No se puede reservar')
        self._estado     = EstadoMaterial.RESERVADO
        self._lector_dni = dni_lector


    def dar_de_baja(self) -> None:
        if self._estado == EstadoMaterial.PRESTADO:
            raise PermissionError('No se puede dar de baja un libro prestado')
        self._estado = EstadoMaterial.BAJA


    def get_estado(self) -> EstadoMaterial:
        return self._estado


    def get_lector(self) -> str:
        return self._lector_dni
