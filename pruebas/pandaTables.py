import pandas as pd
df = pd.read_csv('DBdatosproyecto2024.csv') 

"""print(df.head())  # View the first few rows
print(df.info())  # Get information about the data types and missing values
print(df.describe())  # Get descriptive statistics"""

"""print(df['Sex'].value_counts())  # Count the number of males and females
print(df['Race'].value_counts())  # Count the occurrences of different races"""

"""print(df.groupby('Race')['Income'].mean())  # Average income by race
print(df[df['HealthInsurance'] == 1]['Age'].mean())  # Average age of those with health insurance"""

import matplotlib.pyplot as plt




