import numpy as np

arr = np.array([1, 2, 3, 4, 5])

num_elements = arr.size

element_bytes = arr.itemsize

total_bytes = num_elements * element_bytes

print("Number of elements:", num_elements)
print("Length of one array element in bytes:", element_bytes)
print("Total bytes consumed by the elements:", total_bytes)
