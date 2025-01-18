import numpy as np
from luus_jaakola import luusJaakola
from evolucao_diferencial import evolucaoDiferencial
from temperaturaMedia import fObj

x, fx = luusJaakola(fObj, [(750, 1000)], 0.01, 200, 200)

print(f"Luus Jaakola -> fObj({x[0]}): {fx}")

x, fx = evolucaoDiferencial(fObj, (750, 1000), 50, 500, 1.3, 0.7)

print(f"Evolução Diferencial -> fObj({x}): {fx}")


# def fObjLuusJaakola(params):
#     params[1] = int(params[1])
#     params[2] = int(params[2])
#     print(f"luusJaakola(coef={params[0]}, nInt={params[1]}, nOut={params[2]})")
#     x, fx = luusJaakola(fObj, [(750, 1000)], params[0], params[1], params[2])

#     print(f"fObj({x[0]}): {fx}")
#     print("-----------------------------------------------")

#     return fx

# x, fx = luusJaakola(fObjLuusJaakola, [(0.001, 0.3), (10, 300), (10, 300)], 0.01, 5, 5)

# print(f"fObjLuusJaakola({x}): {fx}")