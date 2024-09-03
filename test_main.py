import pytest
from main import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada

def test_soma():
    assert soma(3, 5) == 8
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(-1, -1) == 0
    assert subtracao(0, 5) == -5

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-2, 3) == -6
    assert multiplicacao(0, 5) == 0

def test_divisao():
    assert divisao(8, 2) == 4
    assert divisao(9, 3) == 3
    with pytest.raises(ValueError):
        divisao(8, 0)  # Testando erro de divisão por zero

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(10, -1) == 0.1

def test_raiz_quadrada():
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(0) == 0
    with pytest.raises(ValueError):
        raiz_quadrada(-4)  # Testando erro de raiz quadrada de número negativo

if __name__ == "__main__":
    pytest.main()
