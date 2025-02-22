import numpy as np
from temperaturaMedia import pPost

def cadeiaMarkov(bounds, n, sig):
    cadeia = []

    low, high = bounds

    x = np.random.uniform(low, high)

    fx = pPost(x)

    cadeia.append((x, fx))

    for i in range(int(n)):
        prevX, prevFx = cadeia[i]
        newX = np.random.normal(loc=prevX, scale=sig)
        newFx = pPost(newX)

        alfa = np.exp(newFx - prevFx)

        # u = np.log(np.random.uniform(0, 1))
        u = np.random.uniform(0, 1)

        print(f"prevX: {prevX} | newX: {newX} | prevFx: {prevFx} | newFx: {newFx} | alfa: {alfa} | u: {u}")

        if (u <= alfa):
            cadeia.append((newX, newFx))
        else:
            print("-----------------------------------------------------")
            cadeia.append((prevX, prevFx))

    return cadeia