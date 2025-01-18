def digitos(n):
    # Garante que o número é positivo para contar os dígitos
    # Obs: a função 'abs' foi utilizada para simplificação do código, mas poderia ser substituída por uma multiplicação por -1 caso o número fosse negativo
    n = abs(n)

    # Inicializa a quantidade de dígitos como 1 (pelo menos um dígito)
    digitos = 1

    # Enquanto o número for maior ou igual a 10, divide-o por 10 e aumenta a contagem de dígitos
    while n >= 10:
        n //= 10  # Divisão inteira por 10
        digitos += 1  # Aumenta o contador de dígitos
    
    # Retorna o número de dígitos encontrados
    return digitos


def digitosComRecursividade(n):
    # Garante que o número é positivo para contar os dígitos
    # Obs: a função 'abs' foi utilizada para simplificação do código, mas poderia ser substituída por uma multiplicação por -1 caso o número fosse negativo
    n = abs(n)
    
    # Caso base: se o número for menor que 10, retorna 1 (apenas um dígito)
    if n < 10:
        return 1
    
    # Chamada recursiva: divide o número por 10 e adiciona 1 ao número de dígitos
    return 1 + digitosComRecursividade(n // 10)


# Testando para o número 64885
n = 64885

print(f"A quantidade de dígitos do número {n} é: {digitos(n)}")  # Função Iterativa
print(f"A quantidade de dígitos do número {n} é: {digitosComRecursividade(n)}")  # Função Recursiva