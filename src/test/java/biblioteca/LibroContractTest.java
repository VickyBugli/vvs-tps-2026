package biblioteca;

public class LibroContractTest extends MaterialContractTest {

    @Override
    protected Material createMaterial() {
        return new Libro( "1234567890",     // ISBN válido (>=10)
            "Historia del Arte",
            "Carla García",
            2020,
            100               // páginas > 0
        );
    }


// ------------------------- TEST AGREGADOS ---------------------------

    @Test
    void constructor_isbnInvalido_lanzaExcepcion() {
        assertThrows(IllegalArgumentException.class,
            () -> new Libro("123", "Test", "Autor", 2020, 100));
    }

    @Test
    void constructor_paginasInvalidas_lanzaExcepcion() {
        assertThrows(IllegalArgumentException.class,
            () -> new Libro("1234567890", "Test", "Autor", 2020, 0));
    }

    @Test
    void reservar_cambiaEstadoAReservado() {
        Libro libro = new Libro("1234567890", "Test", "Autor", 2020, 100);

        libro.reservar("123");

        assertEquals(EstadoMaterial.RESERVADO, libro.getEstado());
    }

    @Test
    void reservar_noDisponible_lanzaExcepcion() {
        Libro libro = new Libro("1234567890", "Test", "Autor", 2020, 100);

        libro.prestar("123", 5);

        assertThrows(IllegalStateException.class,
            () -> libro.reservar("456"));
    }
}
