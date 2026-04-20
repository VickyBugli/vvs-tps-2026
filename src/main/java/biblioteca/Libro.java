package biblioteca;

public class Libro extends Material {

    private String isbn;
    private String titulo;
    private String autor;
    private int anio;
    private int paginas;
    private String lectorDni;

    public Libro(String isbn, String titulo, String autor, int anio, int numPaginas) {
        if (isbn == null || isbn.length() < 10)
            throw new IllegalArgumentException("ISBN inválido");

        if (numPaginas <= 0)
            throw new IllegalArgumentException("num_paginas debe ser positivo");

        this.isbn = isbn;
        this.titulo = titulo;
        this.autor = autor;
        this.anio = anio;
        this.paginas = numPaginas;
        this.estado = EstadoMaterial.DISPONIBLE;
        this.lectorDni = null;
    }

    @Override
    public String prestar(String dni, int dias) {
        if (dias < 1 || dias > 30)
            throw new IllegalArgumentException("Días inválidos");

        if (estado != EstadoMaterial.DISPONIBLE)
            throw new IllegalStateException("No disponible");

        estado = EstadoMaterial.PRESTADO;
        lectorDni = dni;

        return "Libro prestado a " + dni + " por " + dias + " días";
    }

    @Override
    public void devolver() {
        if (estado != EstadoMaterial.PRESTADO)
            throw new IllegalStateException("No se puede devolver si no está prestado");

        estado = EstadoMaterial.DISPONIBLE;
        lectorDni = null;
    }

    public void reservar(String dniLector) {
        if (estado != EstadoMaterial.DISPONIBLE)
            throw new IllegalStateException("No se puede reservar");

        estado = EstadoMaterial.RESERVADO;
        lectorDni = dniLector;
    }

    public void darDeBaja() {
        if (estado == EstadoMaterial.PRESTADO)
            throw new IllegalStateException("No se puede dar de baja un libro prestado");

        estado = EstadoMaterial.BAJA;
    }

    public EstadoMaterial getEstado() {
        return estado;
    }

    public String getLector() {
        return lectorDni;
    }
}