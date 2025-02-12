import numpy as np
from cadeiaMarkov import cadeiaMarkov
from luus_jaakola import luusJaakola
from temperaturaMedia import fObjVerossimilhanca
from temperaturaMedia import fObjMap

n=1000
sig=917 * 0.005

print(f"Cadeia Markov -> n={n} | sig={sig}")

cadeia = cadeiaMarkov((750, 1000), n, sig)

nInt=200
nOut=200
coef=0.2

x1, fx1 = luusJaakola(fObjVerossimilhanca, [(750, 1000)], coef, nInt, nOut)

print(f"coef={coef} | nInt={nInt} | nOut={nOut}")
print(f"Luus Jaakola Verossimilhança -> fObj({x1[0]}): {fx1}")

nInt=200
nOut=200
coef=0.2

x1, fx1 = luusJaakola(fObjMap, [(750, 1000)], coef, nInt, nOut)

print(f"coef={coef} | nInt={nInt} | nOut={nOut}")
print(f"Luus Jaakola MAP -> fObj({x1[0]}): {fx1}")