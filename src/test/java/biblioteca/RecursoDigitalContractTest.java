package biblioteca;

public class RecursoDigitalContractTest extends MaterialContractTest {

    @Override
    protected Material createMaterial() {
        return new RecursoDigital("http://test.com",
            50);
    }
}