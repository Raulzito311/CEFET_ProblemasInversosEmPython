# Função de ordenação Insertion Sort
def insertionSort(arr):
    # Inicia o índice 'i' em 1, porque o primeiro elemento já é considerado ordenado
    i = 1

    # Enquanto 'i' for menor que o tamanho do array, o loop continua
    while i < len(arr):
        # 'j' começa em 'i' e vai retrocedendo enquanto o valor da célula anterior for maior que o valor atual
        j = i
        # Loop interno para verificar e mover os elementos maiores que arr[j] para a direita
        while j > 0:
            # Se o elemento anterior for maior que o atual, faz a troca
            if (arr[j - 1] > arr[j]):
                aux = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = aux
                # print(arr)  # Se quiser ver a evolução do array, pode descomentar
            # Move o índice 'j' para a esquerda
            j -= 1
        # Move o índice 'i' para a próxima posição
        i += 1
    
    # Retorna o array ordenado
    return arr

# Função de ordenação Selection Sort
def selectionSort(arr):
    # Inicializa o índice 'i' como 0
    i = 0
    # Enquanto 'i' for menor que o tamanho do array, o loop continua
    while i < len(arr):
        # Inicializa o índice 'j' como 'i + 1'
        j = i + 1
        # Loop para percorrer os elementos à direita de arr[i]
        while j < len(arr):
            # Se o elemento atual for maior que o próximo, realiza a troca
            if (arr[i] > arr[j]):
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
                # print(arr)  # Se quiser ver a evolução do array, pode descomentar
            j += 1
        # Move o índice 'i' para a próxima posição
        i += 1
    # Retorna o array ordenado
    return arr

# Array original para ordenação
arr = [5, 2, 8, 9, 5, 4, 3, 7, 7, 0, 1, 6]

# Exibe o array original e a ordenação com Insertion Sort
print(f"Array: {arr}")
print(f"Insertion Sort: {insertionSort(arr)}")

# Outro array para ordenação com Selection Sort
arr2 = [5, 2, 8, 9, 4, 3, 7, 0, 1, 6]

# Exibe o array original e a ordenação com Selection Sort
print(f"Array: {arr2}")
print(f"Selection Sort: {selectionSort(arr2)}")