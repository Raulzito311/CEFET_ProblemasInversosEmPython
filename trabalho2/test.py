import numpy as np

def test(bounds):
    print(f"bounds: {bounds}")

    x = np.array([np.random.uniform(low, high) for low, high in bounds])

    stepSize = np.array([high - low for low, high in bounds])

    newX = x + stepSize

    print(f"x: {x}")
    print(f"stepSize: {stepSize}")
    print(f"newX: {newX}")

    stepSize = np.multiply(stepSize, 0.5)

    print(f"stepsize * 2: {stepSize}")
    print(f"stepsize max: {np.max(stepSize)}")
    print(f"stepsize max < 1.658893: {np.max(stepSize) < 1.658893}")

    

test([(0, 2), (3, 6)])