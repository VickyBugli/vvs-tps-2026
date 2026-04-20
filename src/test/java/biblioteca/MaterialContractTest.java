package biblioteca;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

// Acá definimos un contrato que cualquier implementación de Material debe cumplir. Lo heredan las otras clases. 

@TestMethodOrder(MethodOrderer.MethodName.class) // Ejecuta los test en orden alfabético (nos ayuda a tener orden)
public abstract class MaterialContractTest {


    // Cada subclase de test implementa esto y devuelve su tipo concreto
    protected abstract Material createMaterial(); 

    // ── Helpers ──────────────────────────────────────────────────
    private Material disponible() {
        // Se crea un material nuevo y se verifica que arranque en disponible
        Material m = createMaterial();
        assertEquals(EstadoMaterial.DISPONIBLE, m.getEstado());
        return m;
    }

    private Material prestado() {
        // Devuelve un material ya prestado
        Material m = disponible();
        m.prestar("12345678A", 3);
        return m;
    }

    // ── Tests de prestar() ────────────────────────────────────────

    @Test
    void prestar_diasMinimo_retornaConfirmacion() {
        // Verifica que prestar con un dia no falle y devuelva algo
        String result = disponible().prestar("12345678A", 1);
        assertNotNull(result);
    }

    @Test
    void prestar_diasMaximo_retornaConfirmacion() {
        // Revista FALLA: lanza excepción porque 30 > 7
        // El contrato dice que hasta 30 dias deberia funcionar --> pero Revista limita a 7 (se rompe)
        String result = disponible().prestar("12345678A", 30);
        assertNotNull(result);
    }

    @Test
    void prestar_diasValidos_modifAPrestado() {
        // RecursoDigital FALLA: estado queda DISPONIBLE
        // El contrato exige que despues de prestar --> estado = PRESTADO 
        Material m = disponible();
        m.prestar("12345678A", 3);
        assertEquals(EstadoMaterial.PRESTADO, m.getEstado());
    }

    @Test
    void prestar_materialDisponible_noLanzaExcep() {
        assertDoesNotThrow(() -> disponible().prestar("12345678A", 5));
    }

    @Test
    void prestar_diasEnRango_noLanzaExcep() {
        // Revista FALLA: 15 es válido para Material pero Revista rechaza > 7
        assertDoesNotThrow(() -> disponible().prestar("12345678A", 15));
    }

    @Test
    void prestar_diasCero_lanzaExcep() {
        assertThrows(IllegalArgumentException.class,
            () -> prestado().prestar("12345678A", 0));
    }

    @Test
    void prestar_yaPrestado_lanzaExcep() {
        assertThrows(IllegalStateException.class,
            () -> prestado().prestar("99999999Z", 1));
    }

    @Test
    void prestar_diasMayorAlMaximo_lanzaExcep() {
        assertThrows(IllegalArgumentException.class,
            () -> disponible().prestar("12345678A", 31));
    }

    @Test
    void prestar_materialPrestado_diasCero_lanzaExcep() {
        assertThrows(IllegalStateException.class,
            () -> prestado().prestar("12345678A", 0));
    }

    @Test
    void prestar_materialPrestado_diasAlMaximo_lanzaExcep() {
        assertThrows(IllegalStateException.class,
            () -> prestado().prestar("12345678A", 31));
    }

    // ── Tests de devolver() ───────────────────────────────────────

    @Test
    void devolver_materialPrestado_modifADisponible() {
        // RecursoDigital FALLA: estado nunca fue PRESTADO
        Material m = prestado();
        m.devolver();
        assertEquals(EstadoMaterial.DISPONIBLE, m.getEstado());
    }

    @Test
    void devolver_materialPrestado_noLanzaExcep() {
        assertDoesNotThrow(() -> prestado().devolver());
    }

    @Test
    void devolver_materialDisponible_lanzaExcep() {
        // RecursoDigital FALLA: no valida la precondición --> no devolver algo que NO está prestado
        assertThrows(IllegalStateException.class,
            () -> disponible().devolver());
    }

    @Test
    void prestarDevolver_cicloCompleto_estadoConsistente() {
        Material m = disponible();
        m.prestar("12345678A", 5);
        m.devolver();
        assertEquals(EstadoMaterial.DISPONIBLE, m.getEstado());
    }

    @Test
    void devolver_materialPrestado_variasVeces_controlaEstado() {
        Material m = prestado();
        m.devolver();

        assertThrows(IllegalStateException.class, m::devolver);
    }


}