def test_sistema_recebeu_atributo_usuario(sistema):
    assert hasattr(sistema, "usuario")

def test_receber_email_retorna_email_correto(sistema):
    assert sistema.obter_email() == "carlos@email.com"