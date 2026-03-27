import numpy as np

# --- Task 1: Creating NumPy Arrays ---

# 1. A 1D array of integers from 1 to 10
arr_1d = np.arange(1, 11)

# 2. A 2D array of shape (3, 3) with values from 1 to 9
arr_2d = np.arange(1, 10).reshape(3, 3)

# 3. A NumPy array from the list: [10, 20, 30, 40, 50]
arr_list = np.array([10, 20, 30, 40, 50])

# --- Print Results ---
print("1D Array:", arr_1d)
print("Shape:", arr_1d.shape)
print("Data Type:", arr_1d.dtype)
print()

print("2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)
print("Data Type:", arr_2d.dtype)
print()

print("Array from List:", arr_list)
print("Shape:", arr_list.shape)
print("Data Type:", arr_list.dtype)