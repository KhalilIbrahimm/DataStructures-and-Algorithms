def kruskal_algorithm(graph, num_nodes):
    """
    Kruskal's Algorithm using Union-Find to detect and prevent cycles.
    
    Parameters:
    - graph (list): A list of edges represented as tuples (u, v, weight), where u and v are nodes, and weight is the edge weight.
    - num_nodes (int): The number of nodes in the graph.
    
    Returns:
    - MST (list): A list of edges representing the Minimum Spanning Tree.
    """
    
    # Sort edges based on their weight in ascending order
    graph.sort(key=lambda edge: edge[2])
    
    # Initialize Union-Find (disjoint set) data structure
    parent = list(range(num_nodes))
    
    def find(u):
        """
        Find the root of node u with path compression.
        If u is not its own parent, recursively find the root and compress the path.
        """
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        """
        Union the sets containing nodes u and v by connecting their roots.
        """
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    
    MST = []  # List to store the edges of the Minimum Spanning Tree

    # Iterate through sorted edges and build the MST
    for u, v, weight in graph:
        if find(u) != find(v):  # If adding this edge does not form a cycle
            MST.append((u, v, weight))  # Add edge to MST
            union(u, v)  # Union the sets containing u and v
    
    return MST


if __name__ == "__main__":
    # Example edges with (node1, node2, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    # Example graph as a list of edges
    graph_ = [
        (0, 1, 2),  # Edge from node 0 to node 1 with weight 2
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (2, 3, 5)
    ]

    # Print the Minimum Spanning Tree using Kruskal's Algorithm
    print("Edges in the Minimum Spanning Tree are:")
    print(kruskal_algorithm(edges, 4))
