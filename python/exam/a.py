import numpy as np

original_array = np.array([[1, 10, 3], [4, 20, 6], [40, 8, 9]])
print(np.sort(original_array.ravel()))

print(np.sort(original_array,axis=0))
print(np.sort(original_array,axis=1))


