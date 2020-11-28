import pytest

from src.ppp import ejecucion


@pytest.mark.parametrize('opcion1, opcion2', [
    ('papel', 'piedra'),
    ('piedra', 'tijera'),
    ('tijera', 'papel'),
    ('papel', 'tijera')])
def test_papel_gana_piedra(opcion1, opcion2):
    assert opcion1 == ejecucion(opcion1, opcion2)

