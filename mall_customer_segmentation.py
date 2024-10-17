import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import DBSCAN

# Load dataset
df = pd.read_csv("E:/Mall_customers.csv")

# Display initial data
print(df.head())
print(df.tail())

# Encode categorical features
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Age'] = le.fit_transform(df['Age'])
df['Annual Income (k$)'] = le.fit_transform(df['Annual Income (k$)'])
df['Spending Score (1-100)'] = le.fit_transform(df['Spending Score (1-100)'])

# Check for missing values
print("Missing values:", df.isnull().sum().sum())

# Prepare data for clustering
df1 = df.iloc[:, [3, 4]].values

# Visualize the data
plt.scatter(df1[:, 0], df1[:, 1], s=10, c="black")
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=5, min_samples=5)
labels = dbscan.fit_predict(df)

# Visualizing the clusters
plt.scatter(df1[labels == -1, 0], df1[labels == -1, 1], s=10, c='black') 
for i in range(np.max(labels) + 1):
    plt.scatter(df1[labels == i, 0], df1[labels == i, 1], s=10, label=f'Cluster {i}')

plt.legend()
plt.title('DBSCAN Clustering of Mall Customers')
plt.show()
