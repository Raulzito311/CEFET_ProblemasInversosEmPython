def maior(arr):
    # Inicializa a variável 'maior' com o primeiro elemento da lista
    maior = arr[0]

    # Percorre cada elemento 'n' na lista 'arr'
    for n in arr:
        # Se o elemento 'n' for maior que o 'maior' atual, atualiza o valor de 'maior'
        if (n > maior):
            maior = n
    
    # Retorna o maior valor encontrado na lista
    return maior

def maiorComRecursividade(arr):
    # Caso base: se a lista tiver apenas um elemento, esse é o maior valor
    if len(arr) == 1:
        return arr[0]
    
    # Chamada recursiva para encontrar o maior valor na sublista a partir do segundo elemento
    maiorRestante = maiorComRecursividade(arr[1:])

    # Exibe qual é o maior número encontrado na sublista atual
    # print(f"Maior {arr[1:]}: {maiorRestante}")
    
    # Compara o primeiro elemento da lista com o maior valor da sublista restante
    # Retorna o maior valor entre os dois
    return arr[0] if arr[0] > maiorRestante else maiorRestante

# Exemplo de lista de números
arr = [2, 81, 6, 9, 5]

# Chama a função não recursiva para encontrar o maior número na lista e imprime o resultado
print(f"O maior elemento do array {arr} é: {maior(arr)}")

# Chama a função recursiva para encontrar o maior número na lista e imprime o resultado
print(f"O maior elemento do array {arr} é: {maiorComRecursividade(arr)}")