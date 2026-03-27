import numpy as np

# --- Task 6: Percentiles & Sorting ---

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

# 1. Sort the array
sorted_marks = np.sort(marks)
print("Sorted Marks:", sorted_marks)
print()

# 2. Find Percentiles
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))
print()

# 3. Count students who scored above the average
average = np.mean(marks)
above_average = np.sum(marks > average)
print("Average Marks:", average)
print("Students above average:", above_average)