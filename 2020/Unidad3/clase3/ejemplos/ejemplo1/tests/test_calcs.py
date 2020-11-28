from src import calcs


def test_func(mocker):
    mocker.patch.object(
        calcs,  # va el modulo que importamos.
        'CONSTANTE',
        1
    )
    assert 2 == calcs.func()



