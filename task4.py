import numpy as np

# --- Task 4: Aggregation Operations ---

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Array:\n", data)
print()

# 1. Row-wise sum (axis=1)
print("Row-wise Sum:", np.sum(data, axis=1))

# 2. Column-wise sum (axis=0)
print("Column-wise Sum:", np.sum(data, axis=0))

# 3. Minimum value
print("Minimum Value:", np.min(data))

# 4. Maximum value
print("Maximum Value:", np.max(data))

# 5. Overall mean
print("Overall Mean:", np.mean(data))