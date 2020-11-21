import pytest
import sys

from src.ejemplo import suma_1


class TestOperaciones:

    @pytest.mark.parametrize("expected_result, input_value",
        [
            (11, 10),
            (12, 11),
            (0, -1),
            (-1, -2)
        ])
    def test_suma_1(self, expected_result, input_value):
        assert expected_result == suma_1(input_value)

    def test_suma_erroneas(self):
        assert 1 != suma_1(2)

@pytest.mark.parametrize('input_value,',[
    ("hola",),
    (3.4,),
    (False,)
])
def test_suma_1_recibe_enteros(input_value):
    with pytest.raises(ValueError):
        suma_1(input_value)


def test_tmpdir(tmpdir):
    print(tmpdir)
    assert 1