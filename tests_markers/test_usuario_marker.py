# Crie uma classe chamada Usuario que receba os atributos nome e idade por meio
# do construtor __init__. Desenvolva um método chamado maior_de_idade que
# retorne True quando a idade for igual ou superior a 18 anos e False caso contrário.
# Em seguida, crie um arquivo chamado test_usuario.py para desenvolver testes
# automatizados utilizando o Pytest. Implemente uma função chamada
# test_maior_de_idade utilizando o decorator @pytest.mark.skipif para ignorar a
# execução do teste quando a versão do Python for inferior à 3.10. Utilize o módulo
# sys e o atributo sys.version_info para verificar a versão instalada. Informe o motivo
# da condição utilizando o parâmetro reason. Utilize a instrução assert para verificar
# se o método está retornando corretamente os valores booleanos.

import pytest
from exercicios_markers.ex_usuario import Usuario
import sys
@pytest.mark.skipif(
        sys.version_info < (3,10),
        reason= "Versão do Python inferior à 3.10"
)

def test_maior_de_idade():
    assert Usuario("Gabriel", 19).maior_de_idade() == True