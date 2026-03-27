import numpy as np

# --- Task 7: Mini Use Case: Sales Analysis ---

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

print("Daily Sales:", sales)
print()

# 1. Total weekly sales
print("Total Weekly Sales:", np.sum(sales))

# 2. Average daily sales
avg_sales = np.mean(sales)
print("Average Daily Sales:", avg_sales)

# 3. Highest and lowest sales day
print("Highest Sales Day:", days[np.argmax(sales)], "- ₹", np.max(sales))
print("Lowest Sales Day:", days[np.argmin(sales)], "- ₹", np.min(sales))

# 4. Standard deviation of sales
print("Standard Deviation:", np.std(sales))

# 5. Days where sales were above average
above_avg_mask = sales > avg_sales
print("Days Above Average:", days[above_avg_mask])
print("Sales on those days:", sales[above_avg_mask])