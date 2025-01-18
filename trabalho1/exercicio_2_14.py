def bucketSort(arr, qtd_buckets = 0):
    # Exibe o array que será ordenado
    # print(f"Ordenando array: {arr}")

    # Caso o array tenha 1 ou 0 elementos, ele já está ordenado
    if len(arr) <= 1:
        return arr
    
    # Caso o array tenha apenas dois elementos, verifica se precisam ser trocados
    if len(arr) == 2:
        if arr[0] > arr[1]:
            # Troca os elementos se estiverem fora de ordem
            aux = arr[0]
            arr[0] = arr[1]
            arr[1] = aux
        return arr
    
    # Inicializa as variáveis min e max com o primeiro elemento do array
    min = arr[0]
    max = arr[0]
    # Cria uma lista vazia para os buckets
    buckets = []

    # Percorre o array para encontrar os valores mínimo e máximo
    i = 0
    while i < len(arr):
        if arr[i] < min:
            min = arr[i]

        if arr[i] > max:
            max = arr[i]
        i += 1

    # Se os valores mínimo e máximo forem iguais, não há necessidade de ordenar
    if max == min:
        return arr

    # Se qtd_buckets não for fornecido, define o número de buckets como o tamanho do array
    if qtd_buckets == 0:
        qtd_buckets = len(arr)

    # Cria a quantidade de buckets necessária (lista de listas vazias)
    i = 0
    while i < qtd_buckets:
        buckets.append([])
        i += 1
    
    # Calcula o intervalo (step) entre os buckets
    step = (max - min) / qtd_buckets

    # Distribui os elementos nos buckets com base no intervalo (step)
    for n in arr:
        # Calcula o índice do bucket onde o número será inserido
        bkt_i = (n - min) // step

        # Garantir que o índice do bucket não ultrapasse a quantidade de buckets
        if bkt_i >= qtd_buckets:
            bkt_i -= 1
        
        # Adiciona o número ao bucket correspondente
        buckets[int(bkt_i)].append(n)

    # Exibe os buckets formados
    # print(f"buckets: {buckets}")

    # Ordena recursivamente cada bucket individualmente
    i = 0
    while i < qtd_buckets:
        # A recursão acontece aqui: chama bucketSort para ordenar os buckets
        # O parâmetro qtd_buckets é 0 para que o algoritmo use a quantidade original de buckets
        buckets[i] = bucketSort(buckets[i],  0 if qtd_buckets == len(arr) else qtd_buckets)
        i += 1
    
    # Combina os elementos de todos os buckets ordenados em um array final
    result = []
    for bucket in buckets:
        for n in bucket:
            result.append(n)

    # Retorna o array ordenado
    return result


# Exemplo de uso da função bucketSort
arr = [5, -2.2, 4.9, -1.5, 99, -4, 3.2, -3.5, 1.7, -1.8, 1.6, 1.5]

# Exibe o array original e o array ordenado após a aplicação do algoritmo
print(f"Array: {arr}")
print(f"Ordenado: {bucketSort(arr, 4)}")