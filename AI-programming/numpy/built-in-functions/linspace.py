import numpy as np

print("Create a rank 1 ndarray that has 10 integers evenly spaced \
      between 0 and 25.")
x = np.linspace(0, 25, 10)

# Print the ndarray
print()
print("x = ", x)
print()


# Print information about the ndarray
print("x has dimensions: ", x.shape)
print("x is an object of type: ", type(x))
print("The elements in x are of type: ", x.dtype)


print()
print("============================================================")
print()

print("Create a rank 1 ndarray that has 10 integers evenly spaced \
      between 0 and 25, with 25 excluded.")
x = np.linspace(0, 25, 10, endpoint=False)

# Print the ndarray
print()
print("x = ", x)
print()


# Print information about the ndarray
print("x has dimensions: ", x.shape)
print("x is an object of type: ", type(x))
print("The elements in x are of type: ", x.dtype)


