from cadeiaMarkov import cadeiaMarkov
from luus_jaakola import luusJaakola
from temperaturaMedia import fObjVerossimilhanca
from temperaturaMedia import fObjMap
import matplotlib.pyplot as plt

nInt=100
nOut=100
coef=0.2

x1, fx1 = luusJaakola(fObjVerossimilhanca, [(750, 1000)], coef, nInt, nOut)

print(f"coef={coef} | nInt={nInt} | nOut={nOut}")
print(f"Luus Jaakola Verossimilhança -> fObj({x1[0]}): {fx1}")

x2, fx2 = luusJaakola(fObjMap, [(750, 1000)], coef, nInt, nOut)

print(f"coef={coef} | nInt={nInt} | nOut={nOut}")
print(f"Luus Jaakola MAP -> fObj({x2[0]}): {fx2}")

n=1000
sig=917 * 0.1

print(f"Cadeia Markov -> n={n} | sig={sig}")

for i in range(10):
    cadeia = cadeiaMarkov((750, 1000), n, sig)

    # plt.plot([x for x, fx in cadeia], [fx for x, fx in cadeia])
    plt.plot([x for x, fx in cadeia])
plt.show()





