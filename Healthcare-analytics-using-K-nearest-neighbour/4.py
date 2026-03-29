from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def run_knn(k):
    try:
        # Validate K
        if k <= 0:
            raise ValueError("K must be greater than 0.")

        # Load dataset
        iris = load_iris()
        X, y = iris.data, iris.target

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        # Check if k is valid for training size
        if k > len(X_train):
            raise ValueError("K cannot be greater than number of training samples.")

        # Train model
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Output
        print("\n--- Healthcare Prediction Result ---")
        print("Predicted labels:", y_pred)
        print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("System Error:", e)


# --------- User Input Section ---------
while True:
    try:
        k_input = input("Enter value of K: ").strip()

        if not k_input:
            raise ValueError("Input cannot be empty.")

        k = int(k_input)

        run_knn(k)
        break

    except ValueError:
        print("Invalid input! Please enter a valid integer for K.")

    except Exception as e:
        print("Unexpected Error:", e)
