def diagonalPrincipal(matriz):
    # Obtém o tamanho da matriz, ou seja, o número de linhas (assumindo que a matriz é quadrada)
    size = len(matriz)

    # Inicializa a variável 'i' com 0, que será usada para acessar os elementos da diagonal
    i = 0

    # Enquanto 'i' for menor que o tamanho da matriz, o loop continua
    while i < size:
        # Imprime o elemento da diagonal principal da matriz na posição (i, i)
        print(f"Elemento {i}x{i}: {matriz[i][i]}")
        
        # Incrementa 'i' para passar para o próximo elemento da diagonal
        i += 1

# Define uma matriz quadrada 4x4
matriz = [
    [1, 2, 3, 8],
    [4, 5, 6, 6],
    [7, 8, 9, 4],
    [7, 8, 9, 6]
]

# Imprime a mensagem indicando que os elementos da diagonal principal serão mostrados
print("Elementos da diagonal principal:")

# Chama a função para imprimir os elementos da diagonal principal
diagonalPrincipal(matriz)