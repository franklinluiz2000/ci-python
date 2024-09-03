import math

class MathError(Exception):
    """Classe personalizada para exceções matemáticas."""
    pass

def soma(a, b): return a + b

def subtracao(a, b): return a - b

def multiplicacao(a, b): return a * b

def divisao(a, b):  
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(a, b): return a ** b

def raiz_quadrada(a):   
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(a)

def soma_lista(numeros):
    """
    Retorna a soma de uma lista de números.
    """
    if not all(isinstance(i, (int, float)) for i in numeros):
        raise MathError("Todos os elementos devem ser números.")
    return sum(numeros)

def fatorial(n):
  
    if n < 0:
        raise MathError("Fatorial não está definido para números negativos.")
    return math.factorial(n)

def eh_primo(n):

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):

    if n <= 0:
        raise MathError("O número de termos deve ser maior que zero.")    
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

if __name__ == "__main__":
    # Exemplo de uso
    print(f"Soma de 3 e 5: {soma(3, 5)}")
    print(f"Subtração de 10 e 4: {subtracao(10, 4)}")
    print(f"Multiplicação de 2 e 6: {multiplicacao(2, 6)}")
    print(f"Divisão de 8 por 2: {divisao(8, 2)}")
    print(f"Potência de 2 elevado a 3: {potencia(2, 3)}")
    print(f"Raiz quadrada de 16: {raiz_quadrada(16)}")
    print(f"Soma da lista [1, 2, 3, 4, 5]: {soma_lista([1, 2, 3, 4, 5])}")
    print(f"Fatorial de 5: {fatorial(5)}")
    print(f"7 é primo? {eh_primo(7)}")
    print(f"Primeiros 10 números de Fibonacci: {fibonacci(10)}")



   
