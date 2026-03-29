from collections import deque

def bfs(graph, start):
    try:
        if start not in graph:
            raise ValueError("Start node not in graph.")

        visited = set()
        queue = deque([start])

        print("BFS Traversal:")

        while queue:
            node = queue.popleft()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    except Exception as e:
        print("\nError in BFS:", e)


def dfs(graph, node, visited=None):
    try:
        # Fix for mutable default argument bug
        if visited is None:
            visited = set()

        if node not in graph:
            raise ValueError("Start node not in graph.")

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                dfs(graph, neighbor, visited)

    except Exception as e:
        print("\nError in DFS:", e)


# --------- Graph Definition ---------
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# --------- User Input Section ---------
while True:
    try:
        start_input = input("Enter starting node (0-3): ").strip()

        if not start_input:
            raise ValueError("Input cannot be empty.")

        start = int(start_input)

        if start not in graph:
            raise ValueError("Node must be between 0 and 3.")

        bfs(graph, start)

        print("\nDFS Traversal:")
        dfs(graph, start)

        break

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)
