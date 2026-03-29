from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
import numpy as np

def run_clustering(k):
    try:
        # Validate k
        if k <= 0:
            raise ValueError("Number of clusters must be greater than 0.")

        # Load dataset
        iris = load_iris()
        X = iris.data
        y = iris.target

        # Apply K-Means
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(X)

        # Adjust cluster labels to match actual labels
        labels = np.zeros_like(clusters)

        for i in range(k):
            mask = (clusters == i)

            if np.sum(mask) == 0:
                continue  # skip empty clusters

            labels[mask] = mode(y[mask], keepdims=True)[0][0]

        # Calculate accuracy
        accuracy = accuracy_score(y, labels)

        print("\n--- Clustering Results ---")
        print("Number of clusters:", k)
        print("Clustering Accuracy:", round(accuracy, 2))

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("System Error:", e)


# --------- User Input Section ---------
while True:
    try:
        k_input = input("Enter number of clusters: ").strip()

        if not k_input:
            raise ValueError("Input cannot be empty.")

        k = int(k_input)

        run_clustering(k)
        break

    except ValueError:
        print("Invalid input! Please enter a valid integer (e.g., 3).")

    except Exception as e:
        print("Unexpected Error:", e)
