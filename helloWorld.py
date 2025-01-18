print("Hello world!")

print(2**1)
print(2**2)
print(2**3)
print(2**4)
print(2**5)

pi = 33.1416

print(f"PI: {pi:.3f}")

idade = 21

if idade >= 21:
    print("Maior de idade nos EUA")
elif idade >= 18:
    print("Maior de idade no Brasil")
else:
    print("Menor de idade")

contador = 1

while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1

for i in range(10, 1, -1):
    print(i)

def dividir(numerador, denomidador):
    return numerador / denomidador

while True:
    try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        if denominador != 0:
            print(f"O resultado da divisão é: {dividir(numerador, denominador)}")
            break
        else:
            print("O denominador não pode ser 0")
    except ValueError:
        print("Por favor, digite um numero inteiro válido.")