import numpy as np

print("Create a a rank 1 ndarray with sequential integers \
      from 0 to 19 and reshape it to a 4 x 5 array ")
Y = np.arange(20).reshape(4, 5)

# Print Y
print()
print("Y = \n", Y)
print()

# Print information about Y
print("Y has dimensions: ", Y.shape)
print("Y is an object of type: ", type(Y))
print("The elements in Y are of type: ", Y.dtype)

print()
print("=======================================================")
print()


print("Create a rank 1 ndarray with 10 integers evenly spaced \
      between 0 and 50, with 50 excluded. We then reshape it \
      to a 5 x 2 ndarray")

X = np.linspace(0, 50, 10, endpoint=False).reshape(5,2)


# Print X
print()
print("X = \n", X)
print()


# Print information about X
print("X has dimensions: ", X.shape)
print("X is an object of type: ", type(X))
print("The elements of X are of type: ", X.dtype)

