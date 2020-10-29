import numpy as np

# Create a 3x4 ndarray full of zeros.
X = np.zeros((3, 4))

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

# Create a 3x2 ndarray full of ones.
X = np.ones((3, 2))

# Print X
print()
print("X = \n", X)
print()

# Print information about X
print("X has dimensions: ", X.shape)
print("X is an pbject of type: ", type(X))
print("The elements in X are of type: ", X.dtype)


print()
print("===================================================")
print()

# Create a 2x3 ndarray full of fives
X = np.full((2, 3), 5)

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

# Create a 5x5 Identity matrix
X = np.eye(5)

# Print X
print()
print("X = \n", X)
print()

# Print information about X
print("X has dimensions: ", X.shape)
print("X is an object of type: ", type(X))
print("The elements in X are of type: ", X.dtype)

print()
print("==============================================================")
print()

# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
X = np.diag([10, 20, 30, 40])

print()
print("X = \n", X)
print()
