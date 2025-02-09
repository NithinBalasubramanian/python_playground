import numpy as np

arranged_array = np.arange(1, 12, 2)
# (1 = start from , 10 = upto, 2 is gap between) 

print("arange method array", arranged_array)
print("reshaped arange array", arranged_array.reshape((3,2)))

list_array = np.array([8,2,3,4,5, 7])

print("list method array", list_array)

added_array = np.add(arranged_array, list_array)

print("sum of arrays", added_array)
print("total sum in the array", added_array.sum())
print("mean value", added_array.mean())
print("min value", added_array.min())
print("max value", added_array.max())
# print("max - min val ptp", added_array.ptp())
print("min value stored in", added_array.argmin())
print("max value stored in", added_array.argmax())
print("subtract of arrays", np.subtract(arranged_array, list_array))
print("multiply of arrays", np.multiply(arranged_array, list_array))

random_array  = np.random.rand(2, 2, 2)

print("random array", random_array)
print("repeat array", np.repeat(random_array, 2, axis=1))
print("flatter the array", random_array.reshape(random_array.size))
print("flatter the array using flatten", random_array.flatten()) # inmutable not change orginal
print("flatter the array using ravel", random_array.ravel()) #mutable changes orginal
print("last_array", random_array[-1])
print("sum of column of random last array", random_array[-1].sum(0))
print("sum of column of random last array rows", random_array[-1].sum(axis=1))
print("size of array", random_array.size)
print("randam array dtype", arranged_array.dtype)

print("sort", np.sort(list_array)[::-1]) 
# decending order sort


list_array = np.append(list_array, [12, 7 , 6])

print("appended array", list_array)

np.save("./files/generated/numpy-generation/list_array", list_array)
# save generated array to the path 

# save the array 

loaded_array = np.load("./files/generated/numpy-generation/list_array.npy")

# load from saved file from path

print(loaded_array)

# once_array = np.ones(2) # this creates array as float
ones_array = np.ones(2,dtype = int) #int based array or any dtype needed can be created
# once_array = np.ones((2,2)) #dimention based array creation
zeros_array = np.zeros(2,dtype = int) 

print("ones array", ones_array)
print("unique", np.unique(ones_array))
print("zeros array", zeros_array)


existing_array = np.array([[1, 2, 3], [4, 5, 6]])


zeros_like = np.zeros_like(existing_array)
print("\nZeros like existing array:\n", zeros_like)

ones_like = np.ones_like(existing_array)
print("\nOnes like existing array:\n", ones_like)

zeros_fill = np.zeros((2,3), dtype=np.int8)
zeros_fill[:] = 2
print("\nZeros filled with 2", zeros_fill)
full_array = np.full((2,3), 7) # 2x3 array filled with 7
print("\nArray filled with 7:\n", full_array)

combined_array = np.concatenate((np.ones((3,3), dtype=int), np.zeros((3,3), dtype=int)), axis=0) 
# Concatenate along columns (axis 1) by crows (axis = 0)
print("\nCombined array:\n", combined_array)
print("unique", np.unique(combined_array))
print("unique axis 0\n", np.unique(combined_array, axis=0))
print("unique axis 1\n", np.unique(combined_array, axis=1))

array_test = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("test array:\n", array_test)
print("diagonal values", np.diagonal(array_test))
print("diagonal values offset", np.diagonal(array_test, offset=-1))

print("change to list", array_test.tolist())

print("swap:\n", np.swapaxes(array_test, 0, 1))
print("transpos , same as swap\n", array_test.transpose(0, 1) ,array_test.T)

array_test.tofile("./files/generated/numpy-generation/generated_array.txt", sep=",")
print("save as txt file")
