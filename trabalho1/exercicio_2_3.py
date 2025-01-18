def legal(n):
    # Converte o valor absoluto de 'n' para uma string para tratar o número de forma mais fácil
    # Obs: a função 'abs' foi utilizada para simplificação do código, mas poderia ser substituída por uma multiplicação por -1 caso o número fosse negativo
    s = str(abs(n))

    # Inicializa a variável 'soma' que irá acumular a soma dos dígitos ímpares
    soma = 0

    # Itera sobre cada caractere da string 's'
    for c in s:
        # Converte o caractere para inteiro
        d = int(c)

        # Verifica se o dígito 'd' é par
        if (d % 2) == 0:
            # Se encontrar um dígito par, retorna False, pois o número não é "legal"
            return False
        
        # Se o dígito for ímpar, soma o valor de 'd' à variável 'soma'
        soma += d

    # Após a soma de todos os dígitos ímpares, verifica se a soma é par
    return (soma % 2) == 0

# Define o número 'n' para testar
n = 1135

# Imprime o resultado, informando se o número é "legal" ou não
print(f"O numero {n} é legal? {legal(n)}")