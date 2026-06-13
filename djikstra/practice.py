import csv

FILE_NAME = 'routes.csv'

def file_to_adjacency_matrix(filename):
    file = open(filename)
    csv_file_content = csv.DictReader(file)
    
    all_edgs = []
    max_node_index = 0
    
    for row in csv_file_content: 
        start = int(row["Start"])
        end = int(row["End"])
        distance = int(row["Distance"])
        
        all_edgs.append((start, end, distance))
        if start > max_node_index:
            max_node_index = start
        if end > max_node_index:
            max_node_index = end
            
    node_count = max_node_index + 1
    
    adjacency_matrix = []
    for _ in range(node_count):
        row = [0] * node_count
        
        adjacency_matrix.append(row) 
        
    for start, end, distance in all_edgs: 
        adjacency_matrix[start][end] = distance
        adjacency_matrix[end][start] = distance
        
    return {
        "adjacency_matrix": adjacency_matrix,
        "max_node_index": max_node_index,
        "node_count": node_count
    } 


        
        
        
        
result = file_to_adjacency_matrix(FILE_NAME)

adjacency_matrix = result["adjacency_matrix"]
max_node_index = result["max_node_index"]
node_count = result["node_count"]

print(f" Successfully read {node_count} roads from '{FILE_NAME}'")
print(f"Detected {node_count} total locations (Nodes 0 to {max_node_index})\n")
print("=== GENERATED ADJACENCY MATRIX ===")

WHITE_SPACE = "         "
for row in adjacency_matrix:
    print(f"{WHITE_SPACE}{row}")


def calculate_node_degrees(matrix):
    print("--- Graph Metrics: Node Degrees ---")
    for index, row in enumerate(matrix):
        connections = 0
        for edgs in row:
            if edgs > 0:
                connections += 1
        print(f"Node {index} has {connections} direct connections...")
    print("-----------------------------------")
        
        
calculate_node_degrees(adjacency_matrix)

def dijkstra_shortest_path(matrix, start_node):
    num_nodes = len(matrix)
    unknown_number = float('inf')
    # unknown_number = 10000
    

    # Start by assuming all distances are unknown/infinity
    distances = [unknown_number] * num_nodes
    distances[start_node] = 0 # Distance to your starting point is 0
    print("distances ---->>>", distances)

    visited = [False] * num_nodes
    print("visited --->>", visited)

    for _ in range(num_nodes):
        # Find the node with the shortest known distance that we haven't visited yet
        min_dist = unknown_number
        current_node = -1

        for node in range(num_nodes):
            if not visited[node] and distances[node] < min_dist:
                min_dist = distances[node]
                current_node = node

        # Mark this node as finished
        visited[current_node] = True

        # Look at all neighbors of this node and update their distances
        for neighbor, road_length in enumerate(matrix[current_node]):
            if road_length > 0 and not visited[neighbor]:
                new_distance = distances[current_node] + road_length

                # If this new path is a shortcut, save it!
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

# Calculate shortest paths starting from Node 0
shortest_routes = dijkstra_shortest_path(adjacency_matrix, start_node=0)

print("shortest_routes --->>>", shortest_routes)

print("--- Shortest Travel Distances From Node 0 ---")
for node, distance in enumerate(shortest_routes):
    print(f"Shortest distance to Node {node}: {distance} miles/km")