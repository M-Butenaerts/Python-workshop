import numpy as np

arr1 = np.zeros((2,3))
arr2 = np.ones((3,2))

arr2 *= 2
print(arr2)

np.random.seed(4)
arr3 = np.random.randint(0, 1, size=(2,3))
arr4 = np.random.randint(0, 1, size=(2,2))

print(arr4)