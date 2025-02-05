import numpy as np
from cadeiaMarkov import cadeiaMarkov
# from temperaturaMedia import fObj

n=1000
sig=917 * 0.01

cadeia = cadeiaMarkov((750, 1000), n, sig)

print(f"Cadeia Markov -> n={n} | sig={sig}")

for e in cadeia:
    print(f"x = {e[0]} | fx = {e[1]}")
