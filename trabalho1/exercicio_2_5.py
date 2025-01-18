def multiplosDe5MenoresQue(max):
    # Inicializa a variável 'n' com o valor 0, que será utilizado para armazenar os múltiplos de 5
    n = 0

    # Enquanto 'n' for menor que o valor máximo fornecido, o loop continuará
    while n < max:
        # Imprime o valor atual de 'n', que é um múltiplo de 5
        print(n)
        
        # Incrementa 'n' por 5 a cada iteração, assim gerando o próximo múltiplo de 5
        n += 5

# Define o valor máximo para a função
n = 20

# Imprime a mensagem informando o valor máximo utilizado
print(f"Múltiplos de 5 menores que {n}:")

# Chama a função para imprimir os múltiplos de 5 menores que o valor de 'n'
multiplosDe5MenoresQue(n)