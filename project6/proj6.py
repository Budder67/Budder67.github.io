import pandas as pd
import seaborn as sns
import numpy as np

# Project 6: Data Exploration and Visualization
# CS110 - Data Science with Python

import matplotlib.pyplot as plt

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ============================================
# PART 1: Dataset Selection and Exploration
# ============================================

# TODO 1: Load your dataset
# Example: df = pd.read_csv('your_dataset.csv')
# You can also use: pd.read_excel(), pd.read_json(), etc.

# df = pd.read_csv('path_to_your_dataset.csv')

# TODO 2: Initial Data Exploration
# Uncomment and use these when you have loaded your data:
# print("Dataset Shape:", df.shape)
# print("\nColumn Names:")
# print(df.columns)
# print("\nFirst 5 rows:")
# print(df.head())
# print("\nDataset Info:")
# print(df.info())
# print("\nStatistical Summary:")
# print(df.describe())

# ============================================
# PART 2: Data Cleaning (if necessary)
# ============================================

# TODO 3: Check for missing values
# print("\nMissing Values:")
# print(df.isnull().sum())

# Handle missing values if needed:
# df.dropna(inplace=True)  # Remove rows with missing values
# df.fillna(value=0, inplace=True)  # Fill missing values with a specific value

# ============================================
# PART 3: Data Visualization and Analysis
# ============================================

# TODO 4: Create your visualizations
# Example 1: Bar Chart
# plt.figure(figsize=(10, 6))
# df['column_name'].value_counts().plot(kind='bar')
# plt.title('Title of Your Chart')
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.tight_layout()
# plt.show()

# Example 2: Scatter Plot
# plt.figure(figsize=(10, 6))
# plt.scatter(df['column1'], df['column2'])
# plt.title('Title of Your Chart')
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.tight_layout()
# plt.show()

# Example 3: Histogram
# plt.figure(figsize=(10, 6))
# plt.hist(df['column_name'], bins=30, edgecolor='black')
# plt.title('Title of Your Chart')
# plt.xlabel('X-axis Label')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

done = True