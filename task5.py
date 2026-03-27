import numpy as np

# --- Task 5: Statistical Operations (Core Focus) ---

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print("Marks:", marks)
print()

# 1. Mean
print("Mean:", np.mean(marks))

# 2. Median
print("Median:", np.median(marks))

# 3. Variance
print("Variance:", np.var(marks))

# 4. Standard Deviation
print("Standard Deviation:", np.std(marks))

# 5. Minimum & Maximum
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

# 6. Range (max - min)
print("Range:", np.max(marks) - np.min(marks))s