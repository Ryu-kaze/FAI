def optimize_vehicle_load(product_weights, product_profits, vehicle_capacity):
    try:
        n = len(product_profits)

        if n == 0:
            print("Error: No products provided.")
            return

        if len(product_weights) != len(product_profits):
            print("Error: Number of weights and profits must be the same.")
            return

        if vehicle_capacity < 0:
            print("Error: Vehicle capacity cannot be negative.")
            return

        dp = [[0] * (vehicle_capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(vehicle_capacity + 1):
                if product_weights[i - 1] <= w:
                    dp[i][w] = max(
                        product_profits[i - 1] + dp[i - 1][w - product_weights[i - 1]],
                        dp[i - 1][w]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]

        print("Maximum profit loaded into vehicle:", dp[n][vehicle_capacity])

    except Exception as e:
        print("An unexpected error occurred:", e)


# ---- Taking input from user ----
try:
    weights = list(map(int, input("Enter product weights (space separated): ").split()))
    profits = list(map(int, input("Enter product profits (space separated): ").split()))
    capacity = int(input("Enter vehicle capacity: "))

    optimize_vehicle_load(weights, profits, capacity)

except ValueError:
    print("Error: Please enter only integer values.")
except Exception as e:
    print("Input error:", e)
