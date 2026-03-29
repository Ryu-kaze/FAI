from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def run_classification(test_size, kernel_type):
    try:
        # Validate inputs
        if not (0 < test_size < 1):
            raise ValueError("Test size must be between 0 and 1.")

        if kernel_type not in ["linear", "rbf", "poly"]:
            raise ValueError("Invalid kernel type. Choose: linear, rbf, poly.")

        # Load dataset (flower features)
        iris = load_iris()
        X, y = iris.data, iris.target

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        # Train SVM model
        clf = SVC(kernel=kernel_type)
        clf.fit(X_train, y_train)

        # Predictions
        y_pred = clf.predict(X_test)

        # Results
        print("\n--- Botanical Classification Results ---")
        print("Predicted labels:", y_pred)
        print("Actual labels   :", y_test)
        print("Accuracy        :", round(accuracy_score(y_test, y_pred), 2))

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("System Error:", e)


# --------- User Input Section ---------
while True:
    try:
        test_size_input = input("Enter test size (0 < value < 1, e.g., 0.3): ").strip()
        kernel_input = input("Enter SVM kernel (linear / rbf / poly): ").strip().lower()

        if not test_size_input:
            raise ValueError("Test size cannot be empty.")

        test_size = float(test_size_input)

        run_classification(test_size, kernel_input)
        break

    except ValueError:
        print("Invalid input! Enter a decimal like 0.2 or 0.3 and a valid kernel.")

    except Exception as e:
        print("Unexpected Error:", e)
