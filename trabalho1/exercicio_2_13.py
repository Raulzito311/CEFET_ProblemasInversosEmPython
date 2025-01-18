def bubbleSort(arr):
    # Inicializa a variável 'trocou' para garantir que o loop continue enquanto ocorrerem trocas
    trocou = True
    while(trocou):
        # A cada iteração, considera que não houve trocas (trocou = False)
        trocou = False
        # Itera sobre os elementos da lista
        i = 0
        while i < (len(arr) - 1):
            j = i + 1
            # Se o elemento da posição i for maior que o da posição j, troca-os
            if (arr[i] > arr[j]):
                trocou = True
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
                # print(arr)  # Descomente para ver o array em cada troca
            i += 1
    # Retorna a lista ordenada
    return arr

# Testando o algoritmo Bubble Sort
arr = [5, 2, 8, 9, 4, 3, 7, 0, 1, 6]

print(f"Array: {arr}")
print(f"Ordenado: {bubbleSort(arr)}")
