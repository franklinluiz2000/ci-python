# test_main.py
import pytest
from main import soma

def test_soma():
    """
    Testa a função soma para verificar se está retornando os valores corretos.
    """
    assert soma(3, 5) == 8
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

if __name__ == "__main__":
    pytest.main()
