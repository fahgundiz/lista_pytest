import pytest
from models.ex_cliente import Cliente


@pytest.fixture
def cliente():
    return Cliente("Fernanda","fernanda@email.com", 25)