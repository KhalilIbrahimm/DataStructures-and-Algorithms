from collections import deque

def kahns_algorithm_topological_sort(graph: list, antall_noder: int) -> str:
    """
    Kahn's Algorithm for topological sorting of a Directed Acyclic Graph (DAG).
    
    This algorithm also checks for cycles. If a cycle is detected, it returns a message indicating that the graph is not a DAG.
    
    Parameters:
    - graph (list): A list of edges represented as tuples (from_node, to_node).
    - antall_noder (int): The total number of nodes in the graph.
    
    Returns:
    - str: A topologically sorted list of nodes if the graph is a DAG. 
           Otherwise, a message indicating the presence of a cycle.
    """
    topological_ordered_list = []
    in_degree = {node: 0 for node in range(antall_noder)}

    graph_tuple = {}
    for node in graph:
        in_degree[node[1]] += 1
        if node[0] not in graph_tuple:
            graph_tuple[node[0]] = [node[1]]
        else:
            graph_tuple[node[0]].append(node[1])

    queue = deque([node for node in in_degree if in_degree.get(node) == 0])

    print('Start graph Degree: ', in_degree)
    while queue:
        node = queue.popleft()

        if node in graph_tuple:
            print('node:', node)
            for nabo in graph_tuple[node]:
                in_degree[nabo] -= 1
                if in_degree[nabo] == 0:
                    queue.append(nabo)

        topological_ordered_list.append(node)
        in_degree.pop(node)
        print('topological_ordered_list', topological_ordered_list)
        print('in_degree:', in_degree)

    if len(topological_ordered_list) == antall_noder:
        return f'Topological list = {topological_ordered_list}'  # Topological sorting
    else:
        return 'Cycle detected, this graph is not a DAG and has no topological list.'  # Cycle detected
