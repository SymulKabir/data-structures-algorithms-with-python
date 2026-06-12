# Graph represented by your adjacency matrix:
#       (5)
#     0 ------- 1
#     |         |
#  (2)|         |(4)
#     |         |
#     2 ------- 3
#       (7)


# From This graph the adjacency matrix output will be
#   [0, 5, 2, 0],  # Roads starting from Node 0
#   [5, 0, 0, 4],  # Roads starting from Node 1
#   [2, 0, 0, 7],  # Roads starting from Node 2
#   [0, 4, 7, 0]   # Roads starting from Node 3

import csv
 
FILENAME = "routes.csv"

data = [
    ["Start", "End", "Distance"],
    [0, 1, 5],
    [0, 2, 2],
    [1, 3, 4],
    [2, 3, 7],
]

file = open(FILENAME, "w", newline="") 
writer = csv.writer(file)
writer.writerows(data)
file.close()
# 1. Open and read the CSV file to find out how many nodes we have

all_edges = []
max_node_index = 0


file_content = open(FILENAME, 'r')
# csv.DictReader automatically recognizes the header row (Start, End, Distance)
csv_reader = csv.DictReader(file_content) 

for row in csv_reader: 
    # Convert text from CSV into numbers 
    start = int(row['Start'])
    end = int(row['End'])
    distance = int(row['Distance'])
    # Save this road for later
    all_edges.append((start, end, distance))
    # Keep track of the highest node number to know how big our grid needs to be
    print(f"start: {start}, end: {end}, max_node_index: {max_node_index}")
    if start > max_node_index:
        max_node_index = start
    if end > max_node_index:
        max_node_index = end
         
# The total number of nodes will be the highest index + 1 (since we start counting at 0)
num_nodes = max_node_index + 1
print(f'Total Node: ', num_nodes)


# 2. Create a blank grid (matrix) filled with zeros
adjacency_matrix = []
for i in range(num_nodes):
    row = [0] * num_nodes 
    adjacency_matrix.append(row)


print("all_edges -->", all_edges)
# 3. Fill the matrix using the data we read from the CSV
for start, end, distance in all_edges:
    # Assuming two-way roads:
    print(f"start: {start}, end: {end}")
    adjacency_matrix[start][end] = distance
    adjacency_matrix[end][start] = distance

print("Successfully created adjacency_matrix ")
print("adjacency_matrix --->>", adjacency_matrix)