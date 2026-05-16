# biblioteca/gestor_biblioteca.py
class GestorBiblioteca:
    def __init__(self, notificador):
        self._catalogos = {}   # isbn -> Libro
        self._notificador = notificador


    def registrar(self, libro) -> None:
        if libro.get_isbn() in self._catalogos:
            raise ValueError('ISBN ya registrado')
        self._catalogos[libro.get_isbn()] = libro


    def prestar(self, isbn: str, dni: str, dias: int) -> str:
        if isbn not in self._catalogos:
            raise KeyError('Libro no encontrado')
        resultado = self._catalogos[isbn].prestar(dni, dias)

        try:
            # Agregamos un try para capturar el error de conexion y que continue sin problema
            self._notificador.enviar(
                destinatario=dni,
                asunto='Préstamo confirmado',
                detalle=resultado)

        except ConnectionError:
            # ignora el error
           pass

        return resultado


    def devolver(self, isbn: str) -> None:
        if isbn not in self._catalogos:
            raise KeyError('Libro no encontrado')
        self._catalogos[isbn].devolver()
        self._notificador.enviar(
            destinatario='sistema',
            asunto='Devolución registrada',
            detalle=isbn)


# biblioteca/notificador_email.py
class NotificadorEmail:
    def enviar(self, destinatario: str, asunto: str, detalle: str) -> None:
        # Implementación real: envía email vía SMTP
        pass   # No disponible en entorno de testing
