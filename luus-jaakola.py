import numpy as np

def luusJaakola(func, bounds, maxIter=10000, stepSize=1, tol=1e-6):
    dim = len(bounds)

    x = np.array([np.random.uniform(low, high) for low, high in bounds])

    fx = func(x)

    for i in range(maxIter):
        newX = x + stepSize * (np.random.rand(dim) * 2 - 1)
        newX = np.clip(newX, [low for low, high in bounds], [high for low, high in bounds])

        newFx = func(newX)

        if newFx < fx:
            x, fx = newX, newFx
        else:
            stepSize *= 0.99

        if stepSize < tol:
            break
    
    return x, fx


def func1(x):
    a, b = x
    return a**4 + b**4 - 3

def func2(x):
    a, b = x
    return 20 + (a**2 - 10 * np.cos(2 * np.pi * a)) + (b**2 - 10 * np.cos(2 * np.pi * b))

def func3(x):
    a, b = x
    return (4 - 2.1 * a**2 + a**4 / 3) * a**2 + a * b + (4 * b**2 - 4) * b**2

def func4(x):
    a, b = x
    return S1(a, b) * S2(a, b)

def S1(a, b):
    return 1 + (a + b + 1)**2 * (19 - 14 * a + 3 * a**2 - 14 * b + 6 * a * b + 3 * b**2)

def S2(a, b):
    return 30 + (2 * a - 3 * b)**2 * (18 - 32 * a + 12 * a**2 + 48 * b - 36 * a * b + 27 * b**2)


print("\nFunção 1")
x, fx = luusJaakola(func1, [(-2, 2), (-2, 2)])
print(f"x = {x}")
print(f"fx = {fx}")

print("\nFunção 2")
x, fx = luusJaakola(func2, [(-4, 4), (-4, 4)])
print(f"x = {x}")
print(f"fx = {fx}")

print("\nFunção 3")
x, fx = luusJaakola(func3, [(-3, 3), (-2, 2)])
print(f"x = {x}")
print(f"fx = {fx}")

print("\nFunção 4")
x, fx = luusJaakola(func4, [(-2, 2), (-2, 2)])
print(f"x = {x}")
print(f"fx = {fx}")