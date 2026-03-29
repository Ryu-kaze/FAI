from collections import deque

def sort_matrix(matrix):
    try:
        if not matrix or not matrix[0]:
            raise ValueError("Matrix cannot be empty.")

        m, n = len(matrix), len(matrix[0])

        # Flatten and sort
        flat = [elem for row in matrix for elem in row]
        flat.sort()

        # Reshape back to matrix
        sorted_matrix = [flat[i*n:(i+1)*n] for i in range(m)]
        return sorted_matrix

    except Exception as e:
        print("Error in sorting matrix:", e)
        return []


def shortest_path(grid, start, target):
    try:
        if not grid or not grid[0]:
            raise ValueError("Grid cannot be empty.")

        m, n = len(grid), len(grid[0])

        # Validate start & target
        if not (0 <= start[0] < m and 0 <= start[1] < n):
            raise ValueError("Start position out of bounds.")
        if not (0 <= target[0] < m and 0 <= target[1] < n):
            raise ValueError("Target position out of bounds.")

        if grid[start[0]][start[1]] != 0 or grid[target[0]][target[1]] != 0:
            raise ValueError("Start/Target must be on free path (0).")

        visited = [[False]*n for _ in range(m)]
        q = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = True

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c, dist = q.popleft()

            if (r, c) == target:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n and
                    not visited[nr][nc] and grid[nr][nc] == 0):

                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))

        return -1  # No path found

    except Exception as e:
        print("Error in path finding:", e)
        return -1


# --------- User Input Section ---------
while True:
    try:
        m = int(input("Enter number of rows: ").strip())
        n = int(input("Enter number of columns: ").strip())

        if m <= 0 or n <= 0:
            raise ValueError("Dimensions must be greater than 0.")

        matrix = []
        print("Enter storage rack values row-wise:")
        for i in range(m):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != n:
                raise ValueError("Each row must have exactly", n, "values.")
            matrix.append(row)

        robot_grid = []
        print("Enter robot navigation grid (0 = free, 1 = blocked):")
        for i in range(m):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != n:
                raise ValueError("Each row must have exactly", n, "values.")
            robot_grid.append(row)

        start_input = input("Enter start position (row col): ").split()
        target_input = input("Enter target position (row col): ").split()

        if len(start_input) != 2 or len(target_input) != 2:
            raise ValueError("Enter exactly two values for positions.")

        start = (int(start_input[0]), int(start_input[1]))
        target = (int(target_input[0]), int(target_input[1]))

        # Process
        sorted_matrix = sort_matrix(matrix)

        print("\n--- Warehouse Storage Optimization ---")
        print("Sorted Storage Matrix:")
        for row in sorted_matrix:
            print(row)

        distance = shortest_path(robot_grid, start, target)

        print("\n--- Robot Navigation ---")
        if distance == -1:
            print("No valid path to target location.")
        else:
            print("Shortest path to target:", distance)

        break

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)
