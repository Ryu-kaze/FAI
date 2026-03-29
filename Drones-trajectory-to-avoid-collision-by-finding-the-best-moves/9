def minimax(position, depth, alpha, beta, maximizingDrone):
    try:
        # Terminal condition
        if depth == 0 or not isinstance(position, list):
            if not isinstance(position, (int, float)):
                raise ValueError("Invalid score value in leaf node.")
            return position

        if maximizingDrone:
            maxEval = float('-inf')

            for move in position:
                eval = minimax(move, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, maxEval)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

            return maxEval

        else:
            minEval = float('inf')

            for move in position:
                eval = minimax(move, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, minEval)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

            return minEval

    except Exception as e:
        print("Error during drone decision computation:", e)
        return 0


# --------- User Input Section ---------
while True:
    try:
        branches_input = input("Enter number of possible drone moves: ").strip()

        if not branches_input:
            raise ValueError("Input cannot be empty.")

        branches = int(branches_input)

        if branches <= 0:
            raise ValueError("Number of moves must be greater than 0.")

        possible_moves = []

        for i in range(branches):
            move_input = input(f"Enter evaluation scores for move {i+1}: ").strip()

            if not move_input:
                raise ValueError("Move scores cannot be empty.")

            values = list(map(float, move_input.split()))

            if not values:
                raise ValueError("Each move must have at least one score.")

            possible_moves.append(values)

        # Run Minimax with Alpha-Beta pruning
        best_score = minimax(
            possible_moves,
            depth=2,
            alpha=float('-inf'),
            beta=float('inf'),
            maximizingDrone=True
        )

        print("\n--- Drone Navigation Decision ---")
        print("Best achievable move score for the drone:", best_score)

        break

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)
