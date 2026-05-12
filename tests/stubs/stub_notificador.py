class NotificadorStub:
    def __init__(self):
        self.envios = [] 
        # Usamos una lista donde guardamos los pedidos 

    def enviar(self, destinatario, asunto, detalle):
        # formato de pedido
        self.envios.append({
            'destinatario': destinatario,
            'asunto': asunto,
            'detalle': detalle
        })