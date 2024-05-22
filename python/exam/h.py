import pandas as pd

# Sample data
data = {'X': [78, 85, 96, 80, 86],
        'Y': [84, 94, 89, 83, 86],
        'Z': [86, 97, 96, 72, 83]}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate element-wise powers
powers = df.pow(df['Z'], axis=0)

# Display the result
print(powers)


import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create scatter plot
plt.scatter(math_marks, science_marks)

# Set labels and title
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot - Mathematics vs Science')

# Set the range of axes
plt.xlim(0, 100)
plt.ylim(0, 100)

# Display the marks range as reference lines
plt.plot(marks_range, marks_range, color='red', linestyle='--')

# Show the plot
plt.show()
