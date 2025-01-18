def divide(n):
    # Converte o valor absoluto de 'n' para uma string para tratar o número de forma mais fácil
    # Obs: a função 'abs' foi utilizada para simplificação do código, mas poderia ser substituída por uma multiplicação por -1 caso o número fosse negativo
    s = str(abs(n))

    # Inicializa a variável 'result' como uma string vazia
    result = ''

    # Itera sobre cada caractere da string 's' (cada dígito do número)
    for c in s:
        # Converte o caractere 'c' para um número inteiro
        d = int(c)

        # Divide o dígito 'd' por 2 e adiciona o resultado à string 'result'
        # A operação 'd // 2' realiza uma divisão inteira, descartando a parte decimal
        result += str(d // 2)

    # Converte a string 'result' de volta para um número inteiro e retorna
    return int(result)

# Define o número 'n' para testar
n = 4712

# Imprime o número original
print(f"Numero: {n}")

# Imprime o resultado da divisão de cada dígito de 'n' por 2
print(f"Dividido: {divide(n)}")