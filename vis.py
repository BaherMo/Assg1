import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('res_dpre.csv')

# Plot a histogram of the 'age' column
plt.hist(data['age'], bins=20, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')

# Save the plot as a PNG file
plt.savefig('vis.png')
plt.show()  # Optionally, display the plot in your Python environment