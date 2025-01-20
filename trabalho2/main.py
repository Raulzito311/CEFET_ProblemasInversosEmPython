from luus_jaakola import luusJaakola
from evolucao_diferencial import evolucaoDiferencial
from temperaturaMedia import fObj

nInt=100
nOut=100
coef=0.2

x1, fx1 = luusJaakola(fObj, [(750, 1000)], coef, nInt, nOut)

print(f"coef={coef} | nInt={nInt} | nOut={nOut}")
print(f"Luus Jaakola -> fObj({x1[0]}): {fx1}")


nPop=10
nGen=100
F=0.25
CR=0.1

x2, fx2 = evolucaoDiferencial(fObj, (750, 1000), nPop, nGen, F, CR)

print(f"nPop={nPop} | nGen={nGen} | F={F} | CR={CR}")
print(f"Evolução Diferencial -> fObj({x2}): {fx2}")
