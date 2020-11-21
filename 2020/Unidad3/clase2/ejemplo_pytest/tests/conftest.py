import pytest
import smtplib


@pytest.fixture(scope='session')
def connection_smtp():
    connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
    code, mensaje = connection.ehlo()
    return code, mensaje
