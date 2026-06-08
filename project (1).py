import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Dataset information
print("\nDataset Info:")
print(df.info())

# Bar Chart
df['gender'].value_counts().plot(kind='bar')
plt.title('Gender Distribution')
plt.show()

# Histogram
df['math score'].plot(kind='hist')
plt.title('Math Score Distribution')
plt.show()

# Pie Chart
df['parental level of education'].value_counts().head(5).plot(
    kind='pie', autopct='%1.1f%%'
)
plt.title('Parental Education')
plt.ylabel('')
plt.show()