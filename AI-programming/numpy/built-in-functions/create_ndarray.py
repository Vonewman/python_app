import numpy as np

print("Create a 4 x 4 ndarray that only constains consecutive even \
      numbers from 2 to 32 (inclusive)")

X = np.linspace(2, 32, 16).reshape(4, 4)

# Print X
print()
print("X = \n", X)
print()


# Print information about X
print("X has dimensions: ", X.shape)
print("X is an object of type: ", type(X))
print("The elements in X are of type: ", X.dtype)
