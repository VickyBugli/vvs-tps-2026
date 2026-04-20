package biblioteca;

public class RecursoDigital extends Material {
    private String url;
    private int tamanioMb;
    private int accesosSimultaneos = 0;
    private static final int MAX_ACCESOS = 5;

    public RecursoDigital(String url, int tamanioMb) {
    this.url = url;
    this.tamanioMb = tamanioMb;
}


    @Override
    public String prestar(String dniLector, int dias) {
        // Los recursos digitales permiten accesos simultáneos
        if (accesosSimultaneos >= MAX_ACCESOS)
            throw new IllegalStateException("Capacidad máxima");
        // No cambia estado a PRESTADO: permanece DISPONIBLE
        accesosSimultaneos++;
        return "Acceso digital habilitado para " + dniLector;
    }


    @Override
    public void devolver() {
        if (accesosSimultaneos > 0) accesosSimultaneos--;
    }
}
