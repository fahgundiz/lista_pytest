import pytest
from models.ex_cliente import Cliente
from models.ex_aluno_curso import Aluno, Curso
from models.ex_usuario_sistema import Usuario, Sistema
from models.ex_estoque import Estoque

@pytest.fixture
def cliente():
    return Cliente("Fernanda","fernanda@email.com", 25)

@pytest.fixture
def aluno():
    return Aluno("Roberto", 8.5)

@pytest.fixture
def curso():
    return Curso("Python", 40)

@pytest.fixture
def usuario():
    return Usuario("Carlos", "carlos@email.com")

@pytest.fixture
def sistema(usuario):
    return Sistema(usuario)

@pytest.fixture(scope= "module")
def estoque():
    return Estoque("Mouse", 10)