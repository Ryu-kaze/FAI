def optimize_delivery_time(initial_time):
    def delivery_time_estimate(time):
        return -(time - 22) ** 2 + 500

    current_time = initial_time

    while True:
        left_neighbor = current_time - 1
        right_neighbor = current_time + 1

        left_value = delivery_time_estimate(left_neighbor)
        right_value = delivery_time_estimate(right_neighbor)
        current_value = delivery_time_estimate(current_time)

        if left_value > right_value:
            best_neighbor = left_neighbor
            best_value = left_value
        else:
            best_neighbor = right_neighbor
            best_value = right_value

        if best_value <= current_value:
            break

        current_time = best_neighbor

    return current_time


# Taking input safely
while True:
    try:
        user_input = input("Enter initial delivery time (number): ")

        # Try converting to float
        initial_time = float(user_input)

        result = optimize_delivery_time(initial_time)
        print("Optimized delivery time value:", result)
        break  # exit loop if success

    except ValueError:
        print("Invalid input! Please enter a valid number (e.g., 10 or 15.5).")

    except Exception as e:
        print("Something went wrong:", e)
