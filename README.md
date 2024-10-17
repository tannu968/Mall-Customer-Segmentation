# Mall Customer Segmentation

This project performs customer segmentation for a mall using the DBSCAN clustering algorithm. The dataset contains information about customers including gender, age, annual income, and spending score.

## Dataset

The dataset `Mall_customers.csv` includes the following columns:
- **CustomerID**: Unique identifier for each customer
- **Gender**: Gender of the customer (Male/Female)
- **Age**: Age of the customer
- **Annual Income (k$)**: Annual income of the customer in thousands of dollars
- **Spending Score (1-100)**: Score assigned by the mall based on customer behavior and spending nature

## Requirements

To run this project, you need the following Python packages:
- numpy
- pandas
- matplotlib
- scikit-learn

You can install them using pip:
```bash
pip install numpy pandas matplotlib scikit-learn

Usage

git clone https://github.com/yourusername/mall-customer-segmentation.git

Navigate to the project directory:
cd mall-customer-segmentation

Run the Python script:
python mall_customer_segmentation.py

Visualization
The script generates a scatter plot visualizing the clusters identified by the DBSCAN algorithm, allowing you to see how customers are segmented based on their income and spending score.

