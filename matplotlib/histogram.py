import matplotlib.pyplot as plt
import numpy as np

from random import sample
data = sample(range(1, 1000), 100)
print(data)

plt.hist(data, bins=10)  # You can specify the number of bins (bars) in the histogram
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')

plt.show()  # Display the histogram