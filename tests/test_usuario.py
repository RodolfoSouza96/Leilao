from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def rodolfo():
    return Usuario('Rodolfo', 100.0)

@pytest.fixture()
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(rodolfo, leilao):
    rodolfo.propoe_lance(leilao, 50.0)

    assert rodolfo.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(rodolfo, leilao):
    rodolfo.propoe_lance(leilao, 1.0)

    assert rodolfo.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(rodolfo, leilao):
    rodolfo.propoe_lance(leilao, 100.0)

    assert rodolfo.carteira == 0.0

def test_nao_deve_permitir_propor_lance_quando_o_valor_da_carteira_for_menor_que_o_valor_do_lance(rodolfo, leilao):
    with pytest.raises(LanceInvalido):

        rodolfo.propoe_lance(leilao, 200.0)
