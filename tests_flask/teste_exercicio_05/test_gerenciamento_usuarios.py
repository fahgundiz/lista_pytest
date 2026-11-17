# Pytest. Implemente testes para verificar se as duas rotas estão funcionando
# corretamente, se retornam o código HTTP 200 e se apresentam as mensagens
# esperadas. Utilize o método test_client() e a instrução assert para validar os
# resultados. Execute os testes pelo terminal utilizando o comando pytest -v, sem
# precisar iniciar manualmente o servidor Flask.

def test_rota_usuarios_retorna_200(app):
    with app.test_client() as client:
        resposta = client.get("/usuarios")

    assert resposta.status_code == 200

def test_rota_usuarios_retorna_msg_correta(app):
    with app.test_client() as client:
        resposta = client.get("/usuarios")

    assert "Lista de usuários" in resposta.get_data(as_text=True)

def test_rota_novo_usuario_retorna_200(app):
    with app.test_client() as client:
        resposta = client.get("/usuarios/novo")

    assert resposta.status_code == 200

def test_rota_novo_usuarios_retorna_msg_correta(app):
    with app.test_client() as client:
        resposta = client.get("/usuarios/novo")

    assert "Cadastro de usuário" in resposta.get_data(as_text=True)
