import numpy as np

print("Create a rank 1 ndarray that has sequential integers from 0 to 9")
x = np.arange(10)

# Print the ndarray
print()
print("x = ", x)
print()


# Print information about the ndarray
print("x has dimensions: ", x.shape)
print("x is an object of type: ", type(x))
print("THe elements in x are of type: ", x.dtype)


print()
print("=================================================================")
print()

print("Create a rank 1 ndarray that has sequential integers from 4 to 9.")
x = np.arange(4, 10)

# Print the ndarray
print()
print("x = ", x)
print()


# Print information about the ndarrray
print("x has dimensions: ", x.shape)
print("x is an object of type: ", type(x))
print("The elements in x are of type: ", x.dtype)

print()
print("===============================================================")
print()

print("Create a rank 1 ndarray that has evenly spaced integers from 1 to 13 \
      in steps of 3.")
# from 1 to 13 in steps of 3.
x = np.arange(1, 14, 3)

# Print the ndarray
print()
print("x = ", x)
print()

# Print Information about the ndarray
print("x has dimensions: ", x.shape)
print("x is an object of type: ", type(x))
print("The elements in x are of type: ", x.dtype)

