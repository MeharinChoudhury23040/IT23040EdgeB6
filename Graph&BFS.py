from collections import deque


# Function to build the graph
def build_graph():
    graph = {}
    edges_no = int(input("Edges no: "))

    for i in range(edges_no):
        edge = input(f"Edge {i + 1}: ").split(", ")
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)  # Since it's an undirected graph

    return graph


# Function to find shortest path using BFS
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                new_path = path + [neighbor]
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)

    return None  # If no path found


# Driver code
graph = build_graph()
print("\nGraph:", graph)

start_node = input("Enter start node: ")
end_node = input("Enter end node: ")

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Shortest path =", " ".join(shortest_path))
else:
    print("No path found")