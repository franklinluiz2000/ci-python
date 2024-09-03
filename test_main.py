import pytest
from main import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, soma_lista, fatorial, eh_primo, fibonacci, MathError


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

def test_soma_lista():
    assert soma_lista([1, 2, 3]) == 6
    assert soma_lista([0, 0, 0]) == 0
    assert soma_lista([1.5, 2.5, 3]) == 7.0
    with pytest.raises(MathError):
        soma_lista([1, 'a', 3])  # Testando erro para elementos não numéricos

def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1
    with pytest.raises(MathError):
        fatorial(-1)  # Testando erro para números negativos

def test_eh_primo():
    assert eh_primo(7) is True
    assert eh_primo(4) is False
    assert eh_primo(1) is False

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
    with pytest.raises(MathError):
        fibonacci(0)  # Testando erro para número inválido

if __name__ == "__main__":
    pytest.main()
