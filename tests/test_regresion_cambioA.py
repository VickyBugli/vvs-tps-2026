import pytest
from biblioteca.libro import Libro, EstadoMaterial
from biblioteca.revista import Revista
from biblioteca.recurso_digital import RecursoDigital


def libro():
    return Libro(
        isbn='9781234567890',
        titulo='Tinker Bell',
        autor='Disney',
        anio=1949,
        num_paginas=300
    )

def revista():
    return Revista(
        numero_edicion=1,
        periodicidad='mensual',
        titulo='National Geographic',
        autor='Varios',
        anio=1950
    )

def recurso():
    return RecursoDigital(
        url='http://ejemplo.com',
        tamanio_mb=100,
        titulo='Manual Python',
        autor='Autor',
        anio=2010
    )


# a) a 21 dias sigue siendo valido

def test_libro_prestar_21_dias_valido():
    l = libro()
    result = l.prestar('12345678', 21)
    assert l.get_estado() == EstadoMaterial.PRESTADO
    assert result is not None

# b) a 22 dias lanza ValueError

def test_libro_prestar_22_dias_lanza_error():
    l = libro()
    with pytest.raises(ValueError):
        l.prestar('12345678', 22)
    assert l.get_estado() == EstadoMaterial.DISPONIBLE  # no quedó prestado

# c) verificar que no se afectan por Libro

def test_revista_no_afectada():
    # Revista tiene su propio límite de 7 días — no depende de Libro
    r = revista()
    r.prestar('12345678', 7)
    assert r.get_estado() == EstadoMaterial.PRESTADO

def test_revista_rechaza_mas_de_7_dias():
    r = revista()
    with pytest.raises(ValueError):
        r.prestar('12345678', 8)

def test_recurso_digital_no_afectado():
    # RecursoDigital no hereda de Libro — el cambio no lo toca
    rd = recurso()
    result = rd.prestar('12345678', 21)
    assert result is not None

def test_recurso_digital_permite_accesos_simultaneos():
    rd = recurso()
    rd.prestar('12345678', 3)
    rd.prestar('82738482', 3)
    assert rd._accesos_simultaneos == 2