package biblioteca;

public class RevistaContractTest extends MaterialContractTest {

    @Override
    protected Material createMaterial() {
        return new Revista(1, "Semanal");
    }
}