def inverte(n):
    # Converte o valor absoluto de 'n' para uma string
    # Obs: a função 'abs' foi utilizada para simplificação do código, mas poderia ser substituída por uma multiplicação por -1 caso o número fosse negativo
    s = str(abs(n))
    
    # Inicializa a variável 'result' como uma string vazia, onde o número invertido será armazenado
    result = ''
    
    # Inicializa 'i' com o índice do último caractere da string 's'
    i = len(s) - 1
    
    # Enquanto 'i' for maior ou igual a 0, continua o loop
    while i >= 0:
        # Adiciona o caractere de índice 'i' da string 's' à variável 'result'
        result += s[i]
        
        # Decrementa 'i' para mover para o próximo caractere à esquerda
        i -= 1

    # Retorna o valor de 'result' convertido de volta para um número inteiro
    return int(result)

# Define o número 'n' para teste
n = 123456789
# Imprime o número original e o resultado invertido
print(f"Numero: {n}")
print(f"Invertido: {inverte(n)}")