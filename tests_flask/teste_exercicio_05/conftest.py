# Crie um pequeno sistema de gerenciamento de usuários utilizando Flask e
# Programação Orientada a Objetos. Desenvolva uma classe chamada
# UsuarioController que receba uma instância da aplicação Flask por meio do
# construtor __init__ e registre duas rotas: /usuarios, responsável por retornar a
# mensagem "Lista de usuários", e /usuarios/novo, responsável por retornar a
# mensagem "Cadastro de usuário". Em seguida, crie uma função chamada
# criar_app para inicializar a aplicação Flask, configurar TESTING=True e registrar o
# UsuarioController. Organize o projeto criando uma pasta chamada tests e um
# arquivo chamado conftest.py para centralizar uma Fixture chamada app,
# responsável por disponibilizar a aplicação configurada aos testes. Crie um arquivo
# chamado test_usuarios.py para desenvolver testes automatizados utilizando o
# Pytest. Implemente testes para verificar se as duas rotas estão funcionando
# corretamente, se retornam o código HTTP 200 e se apresentam as mensagens
# esperadas. Utilize o método test_client() e a instrução assert para validar os
# resultados. Execute os testes pelo terminal utilizando o comando pytest -v, sem
# precisar iniciar manualmente o servidor Flask.

from exercicios_flask.ex_gerenciamento_usuarios import criar_app

import pytest

@pytest.fixture
def app ():
    return criar_app()