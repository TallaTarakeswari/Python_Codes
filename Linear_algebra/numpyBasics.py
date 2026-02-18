import numpy as np
li=[1,2,3]
arr_1d = np.array([1,2,3])  #1D array
arr_row = np.array([[1,2,3]]) #row
arr_col = np.array([[1],[2],[3]]) # columns
print(li)
print(arr_row)
print(arr_col)
print(arr_1d.shape)
print(arr_row.shape)
print(arr_col.shape)


vec_1 = np.array([4,5,6])
vec_2 = np.array([10,20,30])
vec_3 = np.array([1,2])
print(vec_1+vec_2) #vector addition
print(vec_1-vec_2) #vector subtraction
print(vec_1+vec_3) # getting error due to diffent dimentions


