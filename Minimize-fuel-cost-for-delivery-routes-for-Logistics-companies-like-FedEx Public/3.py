from itertools import permutations

def solve_tsp(dist, n):
    try:
        # Validate matrix
        if len(dist) != n or any(len(row) != n for row in dist):
            raise ValueError("Distance matrix must be NxN.")

        cities = list(range(1, n))
        min_cost = float('inf')
        best_path = []

        # Try all possible routes
        for perm in permutations(cities):
            cost = 0

            # From starting city (0) to first city
            cost += dist[0][perm[0]]

            # Between intermediate cities
            for i in range(len(perm) - 1):
                cost += dist[perm[i]][perm[i + 1]]

            # Return to starting city
            cost += dist[perm[-1]][0]

            # Update minimum cost
            if cost < min_cost:
                min_cost = cost
                best_path = (0,) + perm + (0,)

        return best_path, min_cost

    except Exception as e:
        print("Error in TSP computation:", e)
        return [], None


# --------- User Input Section ---------
while True:
    try:
        n_input = input("Enter number of cities: ").strip()

        if not n_input:
            raise ValueError("Input cannot be empty.")

        n = int(n_input)

        if n <= 1:
            raise ValueError("Number of cities must be greater than 1.")

        dist = []
        print("Enter distance matrix row-wise:")

        for i in range(n):
            row = list(map(int, input(f"Row {i+1}: ").split()))

            if len(row) != n:
                raise ValueError(f"Each row must have exactly {n} values.")

            if any(d < 0 for d in row):
                raise ValueError("Distances cannot be negative.")

            dist.append(row)

        best_path, min_cost = solve_tsp(dist, n)

        print("\n--- Optimized Delivery Route ---")
        if best_path:
            print("Optimal Path:", best_path)
            print("Minimum Cost:", min_cost)
        else:
            print("Could not compute optimal path.")

        break

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)
