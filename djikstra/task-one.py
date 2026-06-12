# Graph represented by your adjacency matrix:
#       (5)
#     0 ------- 1
#     |         |
#  (2)|         |(4)
#     |         |
#     2 ------- 3
#       (7)

# Let's create a map with 4 locations: 0, 1, 2, and 3
# Rows and columns represent: [Node 0, Node 1, Node 2, Node 3]

adjacency_matrix = [
    [0, 5, 2, 0],  # Roads starting from Node 0
    [5, 0, 0, 4],  # Roads starting from Node 1
    [2, 0, 0, 7],  # Roads starting from Node 2
    [0, 4, 7, 0]   # Roads starting from Node 3
]

# How to read this matrix:
# print(f"Distance from Node 0 to Node 1: {adjacency_matrix[0][1]}")
# print(f"Distance from Node 0 to Node 3 (no direct road): {adjacency_matrix[0][3]}")

           
def dijkstra(matrix, start):
    n = len(matrix)

    # Step 1: initialize distances
    distances = [float("inf")] * n
    # distances = [float("inf") for item in range(n)] # OR you can you this
    
    visited = [False] * n

    distances[start] = 0

    print("Initial distances:", distances)

    # Step 2: repeat for all nodes
    for _ in range(n):

        # Find the unvisited node with smallest distance
        min_distance = float("inf")
        current_node = -1

        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                current_node = i

        print("\nPicked node:", current_node)

        # mark as visited
        visited[current_node] = True

        # Step 3: update neighbors
        for neighbor in range(n):
            weight = matrix[current_node][neighbor]
            print("======= start ==========")
            print("current_node --->>", current_node)
            print("neighbor --->>", neighbor)
            print("weight --->>", weight)

            if weight > 0 and not visited[neighbor]:
                new_distance = distances[current_node] + weight

                if new_distance < distances[neighbor]:
                    print(f"Update: {current_node} → {neighbor} = {new_distance}")
                    distances[neighbor] = new_distance

        print("Distances now:", distances)

    return distances





result = dijkstra(adjacency_matrix, 0)

print('result ->>>', result)

# for node, distance in enumerate(result):
#     print(f"0 -> {node}: {distance}")