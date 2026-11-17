# Desenvolva uma aplicação Flask que possua uma rota chamada /inicio, 
# responsável por retornar a mensagem "Bem-vindo ao sistema". Utilize uma função 
# chamada criar_app para inicializar a aplicação e registrar a rota. Em seguida, crie 
# um arquivo chamado test_rotas.py para desenvolver testes automatizados 
# utilizando o Pytest. Implemente uma Fixture chamada app utilizando o decorator 
# @pytest.fixture, responsável por criar e configurar a aplicação com TESTING=True. 
# Desenvolva uma função de teste que utilize o recurso test_client() do Flask para 
# acessar a rota /inicio e verificar se a resposta apresenta o código HTTP 200 e a 
# mensagem esperada. Utilize a instrução assert para validar os resultados sem 
# precisar iniciar manualmente o servidor Flask. 
from flask import Flask

def criar_app():
    app = Flask(__name__)
    
    def inicio():
        return "Bem-vindo ao sistema"
    
    app.add_url_rule(
        "/inicio", "inicio", inicio
    )

    return app

if __name__ == "__main__":
    app = criar_app()
    app.run(debug = True)