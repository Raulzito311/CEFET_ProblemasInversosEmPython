import numpy as np

bounds = [(-10, 10), (-10, 10)]
dim = len(bounds)

x = np.array([np.random.uniform(low, high) for low, high in bounds])

print(x)

y = np.random.rand(dim)
print(y)
print(y * 2 - 1)