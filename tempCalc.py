import numpy as np

t = [0, 0.1, 0.2, 0.3, 1000]
A1 = 0.0016
A2 = 0.00192
Tinf = 25
h = 22.491
q = 742.2
p = 903
Ti = 25
V = 1 # get actual value

def tempCalc (cp):
    results = []

    for i in range(len(t)):
        results[i] = Tinf + ((q * A1) / (h * A2)) * (1 - np.exp((-h * A2 * t[i]) / (p * V * cp)))

    return results

def fObj(cp):
    tExp = [20, 20.1, 21,2, 50.2]
    soma = 0
    tCalc = tempCalc(cp)

    for i in range(len(tExp)):
        soma += ((tCalc[i] - tExp[i]) ** 2) / ((tExp[i]) ** 2)
    
    return soma
