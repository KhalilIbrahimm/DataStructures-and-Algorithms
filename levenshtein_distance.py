
def edit_distance(source_word: str, target_word: str) -> int:
    """
    Computes the minimum number of operations required to convert source_word into target_word.
    The allowed operations are:
    - Insertion of a character
    - Deletion of a character
    - Substitution of a character

    Args:
        source_word (str): The initial string to be transformed.
        target_word (str): The final string that we want source_word to match.

    Returns:
        int: The minimum number of operations (insertion, deletion, substitution)
             required to convert source_word to target_word.
    """
    # Dictionary to store the dynamic programming results.
    OPT = {}
    len_source = len(source_word)
    len_target = len(target_word)
    
    # Fill the DP table with optimal values
    for i in range(len_source + 1):
        for j in range(len_target + 1):
            # Base case: If one of the strings is empty, the cost is the length of the other string
            if i == 0 or j == 0:
                OPT[(i, j)] = max(i, j)

            # If characters are the same, no operation is needed
            elif source_word[i - 1] == target_word[j - 1]:
                OPT[(i, j)] = OPT[(i - 1, j - 1)]

            # If characters are different, choose the minimum of three possible operations:
            # 1. Deletion from source_word (reduce i)
            # 2. Insertion into source_word (reduce j)
            # 3. Substitution (replace source_word[i-1] with target_word[j-1])
            else:
                OPT[(i, j)] = min(
                    1 + OPT[(i - 1, j)],    # Deletion from source_word
                    1 + OPT[(i, j - 1)],    # Insertion into source_word
                    1 + OPT[(i - 1, j - 1)] # Substitution
                )
    
    # The result is the minimum number of operations needed to convert source_word to target_word
    return OPT[(len_source, len_target)]

# Example usage
if __name__ == "__main__":
    # Example 1: Simple replacement
    print(edit_distance('Khalil', 'Kahlil'))  # Output: 1

    # Example 2: Multiple operations (substitution, insertion)
    print(edit_distance('kitten', 'sitting'))  # Output: 3

    # Example 3: Deletion only
    print(edit_distance('flaw', 'law'))  # Output: 1

    # Example 4: Insertion only
    print(edit_distance('ball', 'balls'))  # Output: 1

    # Example 5: Completely different words
    print(edit_distance('abc', 'def'))  # Output: 3
