from cadeiaMarkov import cadeiaMarkov
from temperaturaMedia import fObj

n=100
var=0.1

cadeia = cadeiaMarkov(fObj, [(750, 1000)], 10000, var)

print(f"Cadeia Markov -> n={n} | var={var}")

for e in cadeia:
    print(f"i = {e[0]} | x = {e[1]} | fx = {e[2]}")
