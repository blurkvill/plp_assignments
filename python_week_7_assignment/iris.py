# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
try:
    df = pd.read_csv('iris_dataset.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# Task 1: Display and Clean
print("\nFirst 5 rows:\n", df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Drop or fill missing values
df = df.dropna()  # or use df.fillna(method='ffill', inplace=True)

# Task 2: Basic Statistics
print("\nDescriptive Statistics:\n", df.describe())

# Group by species and get mean of each numerical column
if 'species' in df.columns:
    grouped = df.groupby('species').mean(numeric_only=True)
    print("\nMean by Species:\n", grouped)
else:
    print("Column 'species' not found in dataset.")

# Task 3: Visualizations
sns.set_style("whitegrid")

# Line chart: use row index as time
plt.figure(figsize=(10, 4))
plt.plot(df.index, df[df.columns[0]], label=df.columns[0])
plt.title(f'Line Chart of {df.columns[0]} Over Index')
plt.xlabel('Index')
plt.ylabel(df.columns[0])
plt.legend()
plt.show()

# Bar chart: average of one numeric column per species
if 'species' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.barplot(x='species', y=df.columns[2], data=df)
    plt.title(f'Average {df.columns[2]} per Species')
    plt.xlabel('Species')
    plt.ylabel(df.columns[2])
    plt.show()

# Histogram: distribution of one numeric column
plt.figure(figsize=(6, 4))
sns.histplot(df[df.columns[1]], bins=20, kde=True)
plt.title(f'Histogram of {df.columns[1]}')
plt.xlabel(df.columns[1])
plt.show()

# Scatter plot: relationship between two numeric columns
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df.columns[0], y=df.columns[2], hue='species', data=df)
plt.title(f'{df.columns[0]} vs {df.columns[2]}')
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[2])
plt.legend()
plt.show()
