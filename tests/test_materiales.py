import pytest

from biblioteca.revista import Revista
from biblioteca.recurso_digital import RecursoDigital


def test_anio_invalido_revista():

    with pytest.raises(ValueError):
        Revista(
            numero_edicion=15,
            periodicidad='Mensual',
            titulo='National Geographic',
            autor='Varios',
            anio=-1
        )


def test_anio_invalido_recurso_digital():

    with pytest.raises(ValueError):
        RecursoDigital(
            url='https://openai.com',
            tamanio_mb=500,
            titulo='Curso Python',
            autor='OpenAI',
            anio=-1
        )