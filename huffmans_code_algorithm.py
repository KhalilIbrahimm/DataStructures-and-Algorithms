
import heapq
from collections import Counter

# Node class to represent the characters and their frequencies in the Huffman tree
class Node:
    def __init__(self, char, frequency):
        self.char = char  # Character (or None for internal nodes)
        self.frequency = frequency  # Frequency of the character
        self.left = None  # Left child (0)
        self.right = None  # Right child (1)
    
    # To make Node objects comparable by their frequency in a min-heap
    def __lt__(self, other):
        return self.frequency < other.frequency


def huffmans_code(string_input: str) -> dict:
    """
    Implements Huffman's Algorithm to generate binary codes for characters in a string.
    
    Parameters:
    - string_input (str): The input string for which to generate Huffman codes.
    
    Returns:
    - huffman_result (dict): A dictionary mapping each character to its Huffman code.
    """

    # 1. Calculate the frequency of each character in the input string
    frequency = Counter(string_input)

    # 2. Create a heap (priority queue) of nodes for each character
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)  # Organize the heap based on the frequency

    # 3. Build the Huffman tree
    while len(heap) > 1:
        # Extract the two nodes with the lowest frequency
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        # Create a new parent node with these two nodes as children
        merged = Node(None, node1.frequency + node2.frequency)
        merged.left = node1
        merged.right = node2
        
        # Push the new node back into the heap
        heapq.heappush(heap, merged)

    # The Huffman tree is now built, and the root is the only node left in the heap
    huffman_tree_root = heap[0]

    # 4. Generate Huffman codes from the tree
    huffman_result = {}

    def generate_code(node, current_code):
        """
        Recursively generate Huffman codes by traversing the Huffman tree.
        
        Parameters:
        - node (Node): The current node in the Huffman tree.
        - current_code (str): The current binary code (string of 0s and 1s).
        """
        if node is None:
            return
        
        # If we reach a leaf node, store the current binary code for this character
        if node.char is not None:
            huffman_result[node.char] = current_code
            return

        # Traverse left (0) and right (1) children
        generate_code(node.left, current_code + '0')
        generate_code(node.right, current_code + '1')

    generate_code(huffman_tree_root, '')

    return huffman_result


if __name__ == "__main__":
    # Test with a sample input
    test_input = "AABCBCABDAKH"
    huffman_encoder = huffmans_code(test_input)

    print("Huffman Codes for each character:")
    for char, code in huffman_encoder.items():
        print(f"'{char}': {code}")
