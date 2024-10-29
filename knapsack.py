
# Knapsack algorithm - Dynamic Programming


def knapsack(weights: list, values: list, capacity: int) -> int:
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Args:
        weights (list): List of weights for each item.
        values (list): List of values for each item.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be obtained with the given capacity.
    """
    num_items = len(weights)
    # Create a DP table where dp[i][w] is the maximum value for the first i items and capacity w
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, num_items + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: Do not include the item
                # Option 2: Include the item and add its value to the solution for the remaining capacity
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Cannot include the item because it exceeds the capacity
                dp[i][w] = dp[i - 1][w]

    # The last cell of the table will hold the maximum value achievable with the full capacity
    return dp[num_items][capacity]

# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]  # Weights of the items
    values = [3, 4, 5, 6]   # Values of the items
    capacity = 5            # Maximum capacity of the knapsack
    print(knapsack(weights, values, capacity))  # Output: 7 (item 2 and item 1)



