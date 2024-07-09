# from chatgpt

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Priority queue to hold the nodes to be processed
    priority_queue = [(0, start)]
    # To track visited nodes
    visited = set()

    while priority_queue:
        # Find the node with the smallest distance
        current_distance, current_node = min(priority_queue, key=lambda x: x[0])
        priority_queue.remove((current_distance, current_node))
        
        # Skip nodes that have been visited
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Distances from start node:", distances)