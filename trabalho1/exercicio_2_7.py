def somaColunas(matriz):
    # Obtém o número de linhas e colunas da matriz
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Inicializa as variáveis 'i' e 'j' que serão usadas para percorrer as linhas e as colunas
    i = 0
    j = 0

    # Enquanto 'j' for menor que o número de colunas, o loop continua
    while j < colunas:
        # Inicializa a variável 'somaColuna'
        somaColuna = 0
        
        # Loop para percorrer todas as linhas da coluna 'j'
        while i < linhas:
            # Soma o elemento atual da coluna 'j'
            somaColuna += matriz[i][j]
            # Incrementa 'i' para passar para a próxima linha
            i += 1
        
        # Imprime a soma dos elementos da coluna 'j'
        print(f"Soma da coluna {j}: {somaColuna}")
        
        # Reinicia 'i' para 0 e incrementa 'j' para passar para a próxima coluna
        i = 0
        j += 1

# Define uma matriz 2x4 como exemplo
matriz = [ [1, 2, 3, 4], [1, 2, 3, 4] ]

print(f"Soma elementos da coluna:")
# Chama a função para calcular e imprimir a soma das colunas da matriz
somaColunas(matriz)
