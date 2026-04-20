package biblioteca;

public class Revista extends Material {
    private int numeroEdicion;
    private String periodicidad;

    public Revista(int numeroEdicion, String periodicidad) {
    this.numeroEdicion = numeroEdicion;
    this.periodicidad = periodicidad;
}


    @Override
    public String prestar(String dniLector, int dias) {
        // Las revistas solo se prestan por 7 días máximo
        if (estado != EstadoMaterial.DISPONIBLE)
            throw new IllegalStateException();
        if (dias < 1 || dias > 7)   // PRECONDICIÓN MÁS RESTRICTIVA
            throw new IllegalArgumentException("Revistas: máx 7 días");
        estado = EstadoMaterial.PRESTADO;
        return "Revista prestada por" + dias + " días";
    }


    @Override
    public void devolver() {
        if (estado != EstadoMaterial.PRESTADO)
            throw new IllegalStateException("No está prestada");
        estado = EstadoMaterial.DISPONIBLE;
    }
}
