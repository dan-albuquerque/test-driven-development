from src.somador import Somador, SomadorError
import pytest

@pytest.mark.parametrize("op1, op2, resl_esp",[(1,1,2),(3,2,5)])
def test_soma(op1,op2,resl_esp):
    somador = Somador()
    resultado = somador.soma(op1,op2)
    assert resultado == resl_esp


def test_somaDecimal():
    somador = Somador()
    with pytest.raises(SomadorError):
        somador.soma(4.3,1)

def test_somaString():
    somador = Somador()
    with pytest.raises(SomadorError):
        somador.soma("4", 1)
