import numpy as np

print('Create a rank 1 ndarray that contains integrs from 1 to 5')

x = np.array([1, 2, 3, 4, 5])

# Print x
print()
print('x = ', x)
print()

# Accessing to some elements with positive indices
print('This is Fist Element in x: ', x[0])
print('This is Second Element in x: ', x[1])
print('This is Fifth (Last) Element in x: ', x[4])
print()


# Accessing the same elements with negative indices
print('This is First Element in x: ', x[-5])
print('This is Second Element in x: ', x[-4])
print('This is Fifth (Last) Element in x: ', x[-1])

print()
print("===========================================================")
print()

print("Create a rank 1 ndarray that contains integers from 1 to 5")
x = np.array([1, 2, 3, 4, 5])

# We print the original x
print()
print('Original:\n x = ', x)
print()

# We change the fourth element in x from 4 to 20
x[3] = 20

# We print x after it was modified
print('Modified:\n x = ', x)

print()
print('===============================================================')
print()

print('We create a 3x3 rank 2 ndarray that contains integers from 1 to 9')
X = np.arange(1, 10).reshape(3, 3)

# Print X
print()
print('X= \n', X)
print()

# Let's access some elements in X [row, column]
print('This is (0, 0) Element in X: ', X[0, 0])
print('This is (0, 1) Element in X: ', X[0, 1])
print('This is (2, 2) Element in X: ', X[2, 2])


print()
print('===============================================================')
print()

print('Create a 3x3 rank 2 ndarray that contains integers from 1 to 9')
X = np.arange(1, 10).reshape(3, 3)

# Print the original X
print()
print('Original:\n X =\n', X)
print()

print('Change the (0, 0) element in X from 1 to 20')
X[0, 0] = 20

# Print X after it was modified
print('Modified:\n X = \n', X)
