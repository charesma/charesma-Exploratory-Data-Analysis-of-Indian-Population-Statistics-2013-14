import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
path = "C:\\Users\\cherry\\Downloads\\mi_census5_13-14_Table1.10 (1).csv"
df = pd.read_csv(path)


print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.columns)
print(df.shape)
print(df.isnull().sum())
print(df.dropna())
print(df.info())

#Objective 1: Line Chart – Total Issues per State (Simulated Trend)
state_issues = df.groupby('State')[
    ['Salinity - No.', 'Dried up - No.', 'Destroyed beyond repair - No.',
     'Sea water intrusion  - No.', 'Industrial effluents - No.', 'Other reasons - No.']
].sum().sum(axis=1)

plt.figure(figsize=(12, 5))
plt.plot(state_issues.index, state_issues.values, marker='o')
plt.xticks(rotation=90)
plt.title('Total Water Source Issues per State (Simulated Trend)')
plt.xlabel('State')
plt.ylabel('Total Issues')
plt.tight_layout()
plt.show()
