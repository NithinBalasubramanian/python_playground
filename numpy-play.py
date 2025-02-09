import numpy as np

arranged_array = np.arange(1, 10, 2) 

# (1 = start from , 10 = upto, 2 is gap between) 

print("arange method array", arranged_array)

list_array = np.array([8,2,3,4,5])

print("list method array", list_array)

added_array = np.add(arranged_array, list_array)

print("sum of arrays", added_array)
print("subtract of arrays", np.subtract(arranged_array, list_array))
print("multiply of arrays", np.multiply(arranged_array, list_array))

random_array  = np.random.rand(2, 2, 2)

print("random array", random_array)
print("last_array", random_array[-1])
print("size of array", random_array.size)
print("randam array dtype", arranged_array.dtype)

print("sort", np.sort(list_array)[::-1]) 
# decending order sort


list_array = np.append(list_array, [12, 7 , 6])

print("appended array", list_array)

np.save("list_array", list_array)

# save the array 

loaded_array = np.load("list_array.npy")

# load from saved file 

print(loaded_array)