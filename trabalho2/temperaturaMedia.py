import numpy as np
from expData import expData

def tCalc(t, cp):
    a1 = 0.001849 # m^2
    a2 = 0.0023177 # m^2
    v = 5.0385 * (10 ** -6) # m^3
    tInf = 25 # ºC
    h = 21.7 # W / m^2 * K
    tIni = 25 # ºC
    q2 = 742.2 # W / m^2
    p = 2702 # kg / m^3

    if (t == 0):
        return tIni

    x = (q2 * a1) / (h * a2)
    y = 1 - np.exp((-h * a2 * t) / (p * v * cp))
    
    return tInf + x * y

def tMed(cp):
    results = []

    for exp in expData:
        t = exp['t']
        results.append(tCalc(t, cp))

    return results

def fObj(cp):
    tCalc = tMed(cp[0])
    soma = 0

    for i in range(len(expData)):
        soma += ((tCalc[i] - expData[i]['tExp']) ** 2) / (0.07 ** 2)

    return soma


# print(f"tMed: {fObj(917)}")