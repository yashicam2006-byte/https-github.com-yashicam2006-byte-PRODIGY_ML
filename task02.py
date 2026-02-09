

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("Mall_Customers.csv")
print(data.head())

# Select only Annual Income and Spending Score
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Elbow Method (to find best K)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Apply KMeans with K=5
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

# Plot Clusters
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=data['Cluster'])
plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()

# Save output
data.to_csv("Clustered_Customers.csv", index=False)
print("Clustered file saved as Clustered_Customers.csv")

