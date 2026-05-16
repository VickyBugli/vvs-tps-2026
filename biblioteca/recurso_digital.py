# biblioteca/recurso_digital.py

from biblioteca.material import Material
from biblioteca.libro import EstadoMaterial


class RecursoDigital(Material):
    MAX_ACCESOS = 5

    def __init__(self, url: str, tamanio_mb: int,
                 titulo: str, autor: str, anio: int):
        super().__init__(titulo, autor, anio)  # ← valida el año
        self._url = url
        self._tamanio_mb = tamanio_mb
        self._accesos_simultaneos = 0

    def prestar(self, dni_lector: str, dias: int) -> str:
        if self._accesos_simultaneos >= self.MAX_ACCESOS:
            raise RuntimeError("Capacidad máxima")
        self._accesos_simultaneos += 1
        return f'Acceso digital habilitado para {dni_lector}'

    def devolver(self) -> None:
        if self._accesos_simultaneos > 0:
            self._accesos_simultaneos -= 1