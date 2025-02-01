import numpy as np

def cadeiaMarkov(fObj, bounds, n, var):
    dim = len(bounds)

    cadeia = []

    x = np.array([np.random.uniform(low, high) for low, high in bounds])

    fx = fObj(x)

    cadeia.append((-1, x, fx))

    for i in range(int(n)):
        newX = x + var * (np.random.rand(dim) * 2 - 1)
        newX = np.clip(newX, [low for low, high in bounds], [high for low, high in bounds])

        newFx = fObj(newX)

        if newFx < fx:
            x, fx = newX, newFx
            cadeia.append((i, x, fx))

    return cadeia