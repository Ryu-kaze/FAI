def minimax(node, depth, alpha, beta, maximizingPlayer):
    try:
        # Terminal condition (leaf node or depth reached)
        if depth == 0 or not isinstance(node, list):
            if not isinstance(node, (int, float)):
                raise ValueError("Invalid leaf node value.")
            return node

        if maximizingPlayer:
            maxEval = float('-inf')
            for child in node:
                eval = minimax(child, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

            return maxEval

        else:
            minEval = float('inf')
            for child in node:
                eval = minimax(child, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

            return minEval

    except Exception as e:
        print("Error during evaluation:", e)
        return 0


# --------- User Input Section ---------
while True:
    try:
        n = int(input("Enter number of possible moves (branches): ").strip())

        if n <= 0:
            raise ValueError("Number of moves must be greater than 0.")

        tree = []

        for i in range(n):
            user_input = input(f"Enter evaluation scores for move {i+1} (space separated): ").strip()

            if not user_input:
                raise ValueError("Input cannot be empty.")

            values = list(map(float, user_input.split()))

            if not values:
                raise ValueError("Each move must have at least one score.")

            tree.append(values)

        best_score = minimax(
            tree,
            depth=2,
            alpha=float('-inf'),
            beta=float('inf'),
            maximizingPlayer=True
        )

        print("\n--- Chess Training Evaluation ---")
        print("Best achievable score for maximizing player:", best_score)
        break

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

    except Exception as e:
        print("Unexpected Error:", e)
