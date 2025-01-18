def meliante(n):
    # Converte o número 'n' para uma string para facilitar a manipulação dos dígitos
    s = str(n)

    # Inicializa o índice 'i' como 0
    i = 0

    # Enquanto 'i' for menor que o tamanho da string 's', o loop continua
    while i < len(s):
        # Define os índices 'i1' e 'i2' como i+1 e i+2, respectivamente
        i1 = i + 1
        i2 = i + 2

        # Verifica se 'i1' e 'i2' são índices válidos na string
        if (i1 < len(s)) & (i2 < len(s)):
            # Verifica se a sequência de três dígitos consecutivos é "171"
            if (s[i] == '1') & (s[i1] == '7') & (s[i2] == '1'):
                # Se a sequência for "171", retorna True, indicando que o número é meliante
                return True
        
        # Incrementa 'i' para passar para o próximo dígito da string
        i += 1

    # Se nenhuma sequência "171" for encontrada, retorna False
    return False

# Define o número 'n' para testar
n = 12345617789

# Imprime o resultado, informando se o número é meliante ou não
print(f"O numero {n} é meliante? {meliante(n)}")