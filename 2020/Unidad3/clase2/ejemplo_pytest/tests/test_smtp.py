import pytest


def test_code_connection(connection_smtp):
    assert 250 == connection_smtp[0]


def test_mensaje(connection_smtp):
    assert b'smtp' in connection_smtp[1]


@pytest.mark.usefixture("tmpdir")
def test_sin_utilidad():
    assert 1
