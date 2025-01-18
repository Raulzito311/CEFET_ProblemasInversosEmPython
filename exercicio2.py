atrizes = ["Paola Oliveira"]

atrizes.append("Camila Queiroz")

while True:
    nome = input("Digite o nome da atriz: ")
    atrizes.insert(1, nome)
    resp = input("Deseja continuar? [S/N] ")
    if(resp == "N" or resp == "n"):
        break

print(atrizes)