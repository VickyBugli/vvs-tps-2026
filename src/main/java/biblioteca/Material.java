package biblioteca;

public abstract class Material {
    protected String titulo;
    protected String autor;
    protected EstadoMaterial estado = EstadoMaterial.DISPONIBLE;


    // Contrato declarado:
    // Pre: dias >= 1 && dias <= 30 && estado == DISPONIBLE
    // Post: estado == PRESTADO && retorna confirmación no nula


    public abstract String prestar(String dniLector, int dias);


    // Pre: estado == PRESTADO
    // Post: estado == DISPONIBLE && lectorDni == null


    public abstract void devolver();


    public EstadoMaterial getEstado() { return estado; }
}
