def interval_scheduling(intervals: list) -> list:
    """
    Solves the Interval Scheduling Problem - Greedy Algorithm - by selecting the maximum number of non-overlapping intervals.
    
    Parameters:
    - intervals (list): A list of tuples where each tuple represents an interval with a start time and an end time (start, end).
    
    Returns:
    - list: A list of selected intervals that can be scheduled without overlap.
    
    The function uses a greedy algorithm to pick intervals based on their finish times.
    """

    # Sort the intervals by their end times (greedy choice based on the earliest finishing time)
    sort_by_end_time = sorted(intervals, key=lambda interval: interval[1])  # Sort by the end time of each interval

    valid_intervals = []  # List to store the intervals that can be scheduled
    last_end_time = -1  # Keeps track of the end time of the last selected interval

    # Iterate through the sorted intervals
    for interval in sort_by_end_time:
        start_time, end_time = interval  # Unpack the start and end times from each interval
        
        # Select the interval if it starts after the last selected interval ends
        if start_time >= last_end_time:
            valid_intervals.append(interval)  # Add the interval to the valid set
            last_end_time = end_time  # Update the end time of the last selected interval

    return valid_intervals


# Test cases for the algorithm
if __name__ == "__main__":
    scheduling_intervals_1 = [ 
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (8, 9),
        (5, 9),
        (6, 10),
        (2, 14),
        (12, 16)
    ]

    scheduling_intervals_2 = [ 
        (0, 3),
        (1, 3),
        (0, 5),
        (3, 6),
        (4, 7),
        (3, 9),
        (5, 10),
        (8, 10),
    ]

    # Example output
    print("Selected intervals (test case 1):", interval_scheduling(scheduling_intervals_1))
    print("Selected intervals (test case 2):", interval_scheduling(scheduling_intervals_2))
