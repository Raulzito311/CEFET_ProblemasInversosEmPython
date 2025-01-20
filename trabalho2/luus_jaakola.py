import numpy as np

def luusJaakola(func, bounds, coef = 0.01, nInt = 100, nOut = 100):
    dim = len(bounds)

    stepSize = np.array([high - low for low, high in bounds])

    x = np.array([np.random.uniform(low, high) for low, high in bounds])

    fx = func(x)

    for i in range(int(nOut)):
        for j in range(int(nInt)):
            newX = x + stepSize * (np.random.rand(dim) - 0.5)
            newX = np.clip(newX, [low for low, high in bounds], [high for low, high in bounds])


            newFx = func(newX)

            if newFx < fx:
                x, fx = newX, newFx
                print(f"x: {x} | fx: {fx}")
        
        stepSize = np.multiply(stepSize, 1 - coef)

        if (np.max(stepSize) < 10 ** -6):
            return x, fx
    
    return x, fx

