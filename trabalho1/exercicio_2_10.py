def validar(n):
    # Converte o valor absoluto de 'n' para uma string para tratar o número de forma mais fácil
    # Obs: a função 'abs' foi utilizada para simplificação do código, mas poderia ser substituída por uma multiplicação por -1 caso o número fosse negativo
    s = str(abs(n))

    # Se o número tiver apenas um dígito, todos os dígitos são iguais (pois há só um)
    if len(s) <= 1:
        return True
    
    # Se o primeiro dígito for diferente do segundo, retorna False
    if s[0] != s[1]:
        return False
    
    # Chama recursivamente a função, removendo o primeiro dígito e verificando o resto dos dígitos
    return validar(int(s[1:]))  # s[1:] retorna todos os elementos menos o primeiro

# Teste com o número 12345
n = 12345
print(f"Digitos do numero {n} são iguais? {validar(n)}")

# Teste com o número 22222
n = 22222
print(f"Digitos do numero {n} são iguais? {validar(n)}")