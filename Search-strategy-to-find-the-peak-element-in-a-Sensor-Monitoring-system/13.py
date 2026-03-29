import math

def find_peak_and_root(vibrations):
    try:
        # Check if list is empty
        if not vibrations:
            raise ValueError("List cannot be empty.")

        low, high = 0, len(vibrations) - 1
        peak = None

        while low <= high:
            mid = (low + high) // 2

            left = vibrations[mid - 1] if mid > 0 else float('-inf')
            right = vibrations[mid + 1] if mid < len(vibrations) - 1 else float('-inf')

            if vibrations[mid] >= left and vibrations[mid] >= right:
                peak = vibrations[mid]
                break
            elif left > vibrations[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Extra safety check
        if peak is None:
            raise Exception("Peak not found.")

        # Handle negative peak (sqrt issue)
        if peak < 0:
            raise ValueError("Peak is negative, cannot compute square root.")

        peak_root = math.sqrt(peak)

        print("Peak vibration amplitude:", peak)
        print("Square root of peak amplitude:", round(peak_root, 2))

    except ValueError as ve:
        print("Value Error:", ve)

    except Exception as e:
        print("Error:", e)


# ---- Taking input from user safely ----
while True:
    try:
        user_input = input("Enter vibration values (space separated): ").strip()

        if not user_input:
            raise ValueError("Input cannot be empty.")

        vibrations = list(map(float, user_input.split()))

        find_peak_and_root(vibrations)
        break  # exit loop if successful

    except ValueError:
        print("Invalid input! Enter numbers separated by spaces (e.g., 1 2 3 4).")

    except Exception as e:
        print("Something went wrong:", e)
