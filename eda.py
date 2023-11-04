import pandas as pd

# Load the dataset
data = pd.read_csv('res_dpre.csv')  # Replace 'your_dataset.csv' with the actual dataset

# Calculate descriptive statistics
descriptive_stats = data.describe()

# Extract insights
insight_1 = "Insight 1: Summary statistics of the dataset:\n" + descriptive_stats.to_string()
missing_values = data.isnull().sum()
insight_2 = missing_values[missing_values > 0].to_string()
insight_3 = "Insight 3: Correlation between features:\n" + data.corr().to_string()

# Save insights as text files
with open('eda-in-1.txt', 'w') as file:
    file.write(insight_1)

with open('eda-in-2.txt', 'w') as file:
    file.write(insight_2)

with open('eda-in-3.txt', 'w') as file:
    file.write(insight_3)
