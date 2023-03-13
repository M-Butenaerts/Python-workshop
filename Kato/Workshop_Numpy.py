import numpy as np

#array
arr0 = np.zeros((3,3))
arr1 = np.ones((3,2))
arr1 *= 2

# print(arr1)

#index
arr1[0,1] = 3

# print(arr1[0:1,0:2])

#matrix operations
np.random.seed(0)
arr3 = np.random.randint(1, 8, size=(2,3))
arr4 = np.random.randint(1, 8, size=(2,2))


# print(arr4@arr3)
# print(arr4.T)
# print(np.linalg.inv(arr4))


