# Task-02: Customer Segmentation using K-Means Clustering

## 📌 Project Overview
This project is developed as part of *Prodigy Infotech Internship Task-02*.

The main objective of this project is to implement a *K-Means clustering algorithm* to segment customers of a retail store based on their purchase behavior.

Customer segmentation helps businesses understand customer groups and improve marketing strategies.

---

## 📂 Dataset
Dataset used: *Mall Customers Dataset*  
Source: Kaggle  
Link: https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

Dataset contains the following features:
- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

## ⚙️ Technologies Used
- Python
- Google Colab
- Pandas
- Matplotlib
- Scikit-learn

---

## 🧠 Methodology
1. Imported and loaded the dataset.
2. Selected relevant features:  
   - Annual Income (k$)  
   - Spending Score (1-100)
3. Used the *Elbow Method* to find the optimal number of clusters.
4. Applied *K-Means Clustering* with optimal K value.
5. Visualized customer segments using scatter plot.
6. Saved clustered output into a new CSV file.

---

## 📊 Output
- Elbow Method graph to find optimal clusters
- Cluster visualization graph showing customer groups
- Output file generated: Clustered_Customers.csv

---

## 🚀 How to Run the Project
1. Open Google Colab / Jupyter Notebook
2. Upload the dataset file Mall_Customers.csv
3. Run the Python code
4. Clusters will be generated and displayed

---

## 📌 Result
Customers are successfully grouped into different clusters based on their income and spending score, helping in better customer analysis and targeted marketing
