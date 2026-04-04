# Numpy array and basic operations
import numpy as np
import time

arr_1D = np.array([1,2,3,4])
print("The 1D array is :", arr_1D)

arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("The 2D array is :", arr_2D)

print("The shape of 1D array is :", arr_1D.shape) # prints the number of elements
print("The shape of 2D array is :", arr_2D.shape) # prints the number of rows and columns

py_list = [1,2,3]
print("Python list multiplication", py_list*3)

numpy_array = np.array([1,2,3])
print("Numpy array multiplication", numpy_array*3) # element wise multiplication 

# start = time.time()
# py_list = [i * 2 for i in range(100000000)]
# print("\n Python list multiplication time :", time.time() - start)

# start = time.time()
# numpy_array = np.arange(100000000) * 2
# print("\n Numpy array multiplication time :", time.time() - start)

#creating arrays 

zeros = np.zeros((3,4))
print("Zeros array:",zeros)

ones = np.ones((3,4))
print("Ones array:",ones)

full = np.full((3,4),7)
print("Full array:",full)

random = np.random.random((2,2))
print("Random array:",random)

sequence = np.arange(1,10,2)
print("Sequence array:",sequence)

# vector, matrix,tensor

vector = np.array([1,2,3])
print("Vector:",vector)

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("Matrix:",matrix)

tensor = np.array([[[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]]])
print("Tensor:",tensor)

# ARRAY PROPERTIES

arr = np.array([[1,2,3],
                [4,5,6]])
print("Shape:",arr.shape) # no of rows and columns
print("Dimensions:",arr.ndim) # no of dimensions
print("Size:",arr.size) # no of elements
print("Data type:",arr.dtype) # data type of elements


#Array Reshaping

arr1 = np.array([1,2,3,4,5,6])
print("Original array:",arr1)
reshaped = arr1.reshape(2,3)
print("Reshaped array:",reshaped)

flattened = reshaped.flatten() # returns a copy of the original array
print("Flattened array:",flattened)

raveled = reshaped.ravel() # returns a view of the original array
print("Raveled array:",raveled)

transpose = reshaped.T
print("Transpose array:",transpose)


                             