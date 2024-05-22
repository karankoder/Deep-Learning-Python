import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(y, bins=5, color='skyblue')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Bar chart
plt.figure(figsize=(6, 4))
plt.bar(x, y, color='lightgreen')
plt.title('Bar Chart')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Line graph
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', color='orange')
plt.title('Line Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Scatter graph
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='purple',alpha=0.5)
plt.title('Scatter Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
