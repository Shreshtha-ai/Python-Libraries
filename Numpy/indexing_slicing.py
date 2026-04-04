#indexing 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Basic Slicing", arr[2:7])
print("With Step", arr[1:8:2])
print("Negative Indexing",arr[-3])


arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Specific element", arr_2d[1, 2])
print("Entire row: ", arr_2d[1])
print("Entire column:", arr_2d[:,2])

#sorting

unsorted = np.array([1,3,2,4,34,5,6])
print("Sorted array is: ", np.sort(unsorted))

unsorted_2d = np.array([[1,3,2],[4,34,5],[6,7,8]])
print("Sorted 2D array is: ", np.sort(unsorted_2d, axis = 0)) # sorts column wise
print("Sorted 2D array is: ", np.sort(unsorted_2d, axis = 1)) # sorts row wise

#filter

number = np.array([1,2,3,4,5,6,7,8,9,10])
print("Filtered array is: ", number[number % 2 == 0]) 

mask = number >5
print("Masked array is: ", number[mask])

# fance indexing 
indices = np.array([0,2,4])
print(number[indices])

where_result = np.where(number>5) # returns the indices of the elements that satisfy the condition
print(where_result)
print("NP where:",number[where_result])

condition_array = np.where(number>5, "true", "false")
print("Condition array:",condition_array)


#adding 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print("Adding arrays:", arr1 + arr2)

print(np.concatenate((arr1,arr2)))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.array([7, 8, 9])

print("Compatibility shapes", a.shape == b.shape)

original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

with_new_row = np.vstack((original,new_row)) # vstack for row wise addition
print("With new row:",with_new_row)

new_col = np.array([[5],[6]])
with_new_col = np.hstack((original,new_col)) # hstack for column wise addition
print("With new col:",with_new_col)

arr3 = np.array([1,2,3,4,5])
delete = np.delete(arr3,2) # deletes the element at index 2
print("Array after deletion:",delete)


