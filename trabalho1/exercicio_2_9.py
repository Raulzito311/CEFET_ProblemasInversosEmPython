def validar(arr):
    # Inicializa as variaveis soma e multiplicacao
    soma = 0
    multiplicacao = 1
    
    # Inicializa o índice 'i' para percorrer o array
    i = 0
    # Laço para percorrer todos os elementos do array
    while i < len(arr):
        # Armazena o valor do elemento atual
        n = arr[i]

        # Soma o valor do elemento à variável soma
        soma += n

        # Verifica se o índice 'i' é par
        if i % 2 == 0:
            # Se for par, multiplica o valor de 'n' à variável multiplicacao
            multiplicacao *= n

        # Incrementa o índice 'i' para continuar a iteração
        i += 1

    # Exibe a soma de todos os elementos e o produto dos elementos de índice par
    print(f"Soma dos elementos: {soma} | Multiplicação dos elementos de índice par: {multiplicacao}")
    
    # Retorna True se a soma for maior que a multiplicação, caso contrário, retorna False
    return soma > multiplicacao

# Exemplo de array para a função
arr = [2, 8, 6, 9, 5]

# Exibe o resultado da função
print(f"A soma dos elementos do array {arr} é maior do que a multiplicação dos elementos de índice par? {validar(arr)}")