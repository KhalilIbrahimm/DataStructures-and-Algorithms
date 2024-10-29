
from collections import deque

def prims_algorithm(graph: dict) -> tuple:
    """
    Implements Prim's Algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    This is a Greedy Algorithm that expands the tree by choosing the edge with the smallest weight,
    and continues until all nodes are included without creating a cycle.
    
    Parameters:
    - graph (dict): A dictionary representing an undirected graph where keys are nodes and values are dictionaries
                    of neighboring nodes and their edge costs.
    
    Returns:
    - mst (list): A list of edges representing the Minimum Spanning Tree.
    - total_mst_cost (int): The total cost of the MST.
    """
    
    # Start from an arbitrary node
    start_node = next(iter(graph))
    visited_nodes = set([start_node])

    # Create a deque with all edges starting from the start_node
    queue = deque([(start_node, neighbor, edge_cost) for neighbor, edge_cost in graph[start_node].items()])

    mst = []  # Minimum Spanning Tree
    total_mst_cost = 0  # Total cost of MST

    while queue:
        # Remove the edge with the lowest cost
        s_node, e_node, edge_cost = queue.popleft()

        # If the destination node has not been visited
        if e_node not in visited_nodes:
            visited_nodes.add(e_node)  # Mark the node as visited
            mst.append((s_node, e_node, edge_cost))  # Add the edge to the MST
            total_mst_cost += edge_cost  # Add the cost to the total

            # Add all edges from the new node that don't lead to visited nodes
            for neighbor, cost in graph[e_node].items():
                if neighbor not in visited_nodes:
                    queue.append((e_node, neighbor, cost))

    return mst, total_mst_cost


def prims_algorithm_v2(graph: dict, start_node: str) -> tuple:
    """
    Prim's Algorithm for Minimum Spanning Tree (MST) with a specified start node.
    
    This implementation ensures that the deque always processes the edges in order of lowest to highest cost.
    
    Parameters:
    - graph (dict): A dictionary representing the graph (node: {neighbor: edge_cost}).
    - start_node (str): The node to start building the MST from.
    
    Returns:
    - mst (list): The edges that form the Minimum Spanning Tree.
    - total_mst_cost (int): The total cost of the MST.
    """
    
    # Set of visited nodes to prevent cycles
    visited = set([start_node])

    # Deque with all edges starting from the start_node
    queue = deque([(start_node, neighbor, edge_cost) for neighbor, edge_cost in graph[start_node].items()])
    
    mst = []  # Minimum Spanning Tree
    total_cost = 0  # Total cost of the MST

    while queue:
        # Get the next edge with the smallest cost
        s_node, neighbor, edge_cost = queue.popleft()

        # If the neighbor node hasn't been visited
        if neighbor not in visited:
            visited.add(neighbor)  # Mark the neighbor as visited
            mst.append((s_node, neighbor, edge_cost))  # Add the edge to the MST
            total_cost += edge_cost  # Add the edge cost to the total

            # Add all new edges from the current node to the queue
            for next_neighbor, cost in graph[neighbor].items():
                if next_neighbor not in visited:
                    queue.append((neighbor, next_neighbor, cost))
    
    return mst, total_cost


# Example usage of the Prim's Algorithm
if __name__ == "__main__":
    # Define a graph as a dictionary
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Find the MST starting from node 'A'
    mst, mst_cost = prims_algorithm_v2(graph, 'A')
    print('MST:', mst)
    print('MST-cost:', mst_cost)
