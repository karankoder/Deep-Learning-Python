import numpy as np
import matplotlib.pyplot as plt

y=np.linspace(-10,10,100)
x=y**2
plt.bar(x,y)
plt.title("Bar chart for square function")
plt.show()