import random

def objective(x):
    return -(x - 5) ** 2 + 25   # Maximum at x = 5


def hill_climbing(start):
    try:
        if not isinstance(start, int):
            raise ValueError("Starting value must be an integer.")

        current = start
        print("Initial State:", current)

        while True:
            neighbors = [current - 1, current + 1]

            # Choose best neighbor
            next_state = max(neighbors, key=objective)

            # Stop if no improvement
            if objective(next_state) <= objective(current):
                break

            current = next_state

        print("\n--- Optimization Result ---")
        print("Optimal State Found:", current)
        print("Maximum Value:", objective(current))

    except Exception as e:
        print("Error during optimization:", e)


# --------- User Input Section ---------
while True:
    try:
        choice = input("Enter starting value or type 'r' for random: ").strip().lower()

        if choice == 'r':
            start = random.randint(0, 10)

        else:
            if not choice:
                raise ValueError("Input cannot be empty.")
            start = int(choice)

        hill_climbing(start)
        break

    except ValueError:
        print("Invalid input! Enter an integer or 'r'.")

    except Exception as e:
        print("Unexpected Error:", e)
