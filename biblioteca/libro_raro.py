from biblioteca.libro import Libro, EstadoMaterial


class LibroRaro(Libro):

    MAX_DIAS = 7

    def prestar(self, dni: str, dias: int) -> str:
        if dias > self.MAX_DIAS:
            raise ValueError(f"LibroRaro no puede prestarse por más de {self.MAX_DIAS} días")
        super().prestar(dni, dias)

    def reservar(self, dni_lector: str) -> None:
        raise PermissionError("LibroRaro no puede reservarse")