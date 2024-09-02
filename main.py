# main.py
def soma(a, b):
    """
    Retorna a soma de dois números.
    
    Args:
    a (int or float): O primeiro número.
    b (int or float): O segundo número.

    Returns:
    int or float: A soma dos dois números.
    """
    return a + b

if __name__ == "__main__":
    resultado = soma(3, 5)
    print(f"A soma de 3 e 5 é: {resultado}")
