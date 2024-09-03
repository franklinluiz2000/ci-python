import math

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

if __name__ == "__main__":
    # Exemplo de uso
    print(f"Soma de 3 e 5: {soma(3, 5)}")
    print(f"Subtração de 10 e 4: {subtracao(10, 4)}")
    print(f"Multiplicação de 2 e 6: {multiplicacao(2, 6)}")
    print(f"Divisão de 8 por 2: {divisao(8, 2)}")
    print(f"Potência de 2 elevado a 3: {potencia(2, 3)}")
    print(f"Raiz quadrada de 16: {raiz_quadrada(16)}")
