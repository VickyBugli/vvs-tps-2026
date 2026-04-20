package biblioteca;

public enum EstadoMaterial {
    DISPONIBLE("disponible"),
    PRESTADO("prestado"),
    RESERVADO("reservado"),
    BAJA("baja");

    private String valor;

    EstadoMaterial(String valor) {
        this.valor = valor;
    }

    public String getValor() {
        return valor;
    }
}