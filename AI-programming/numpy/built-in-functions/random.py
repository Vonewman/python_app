import numpy as np


print("Create a 3 x 3 ndarray with random floats in the half-open \
      interval [0.0, 1.0).")
"""
X = np.random.random((3, 3))

# Print X
print()
print("x = \n", X)
print()

# Print information about X
print("X has dimensions: ", X.shape)
print("X is an object of type: ", type(X))
print("The elements in X are of type: ", X.dtype)
"""

print()
print("===================================================")
print()


print("Create a 3 x 2 ndarray with random integers in the half-open \
      interval [4, 15).")
X = np.random.randint(4, 15, size=(3, 2))

# Print X
print()
print("X = \n", X)
print()


# Print information about X
print("X has dimensions: ", X.shape)
print("X is an object of type: ", type(X))
print("The elements in X are of type: ", X.dtype)

print()
print("===================================================")
print()

print("create a 1000 x 1000 ndarray of random floats drawn from \
      normal (Gaussian) distribution with a mean of zero and a standard \
      deviation of 0.1.")

X = np.random.normal(0, 0.1, size=(1000,1000))


# print X
print()
print('X = \n', X)
print()

# print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')
# Print X

