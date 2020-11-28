from src import ejemplo


def test_tiempo_de_llamada(mocker):
    mocker.patch(
        'src.ejemplo.expensive_api_call',
        return_value=1
    )
    assert 11 == ejemplo.compute(10)
