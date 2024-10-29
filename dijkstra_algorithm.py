
import math
import heapq

def dijkstra_algorithm(graph, start_node):
    """
    Dijkstra's algorithm finds the shortest path from a start node to all other nodes in the graph.
    
    Parameters:
    - graph (dict): A dictionary representing the graph, where keys are node names and values are dictionaries of neighboring nodes with edge weights.
    - start_node (str): The node from which to start the pathfinding process.

    Returns:
    - distance (dict): A dictionary containing the shortest distance from the start_node to all other nodes.
    - predecessor (dict): A dictionary that maps each node to its predecessor in the shortest path.
    - visited_nodes (list): A list of nodes in the order they were visited.

    The algorithm uses a priority queue (min-heap) to efficiently get the next node with the shortest distance.
    """

    # Initialize distances from start_node to all nodes as infinity
    distance = {node: math.inf for node in graph}  # Example: {'A': inf, 'B': inf, 'C': inf, ...}
    distance[start_node] = 0  # The distance from start_node to itself is always 0

    # Initialize the predecessor dictionary for tracking the path
    predecessor = {node: None for node in graph}

    # Priority queue (heap) to store (distance, node) tuples
    priority_queue = [(0, start_node)]  # Starting with (0, start_node)

    visited_nodes = []  # Track the order of visited nodes

    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the node is already visited, skip it
        if current_node in visited_nodes:
            continue

        # Mark the current node as visited
        visited_nodes.append(current_node)

        # Explore all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited_nodes:
                continue  # Skip already visited neighbors

            # Calculate the new distance to the neighbor
            new_distance = current_distance + weight

            # If a shorter path is found, update the distance and predecessor
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                predecessor[neighbor] = current_node  # Track how we reached this neighbor
                heapq.heappush(priority_queue, (new_distance, neighbor))  # Push the updated distance to the queue

    return distance, predecessor, visited_nodes


# Example usage
if __name__ == "__main__":
    # Define the graph as a dictionary
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }

    # Set the starting node
    start_node = 'A'

    # Run the Dijkstra algorithm
    distances, predecessors, visited_nodes = dijkstra_own(graph, start_node)

    # Print the shortest distances to each node from the start node
    print("Shortest distances from start node:", distances)

    # Print the predecessor of each node in the shortest path
    print("Predecessors in shortest path:", predecessors)

    # Print the order in which nodes were visited
    print("Visited nodes order:", visited_nodes)
