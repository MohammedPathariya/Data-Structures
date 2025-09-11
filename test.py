from typing import List

def solution(tide_levels: List[int]) -> int:
    """
    Counts how many tide readings do not have any future readings with a higher tide.

    This function iterates through the tide levels from right to left, maintaining
    the maximum tide level encountered so far. A reading is counted if it is
    greater than or equal to the maximum of all readings that come after it.

    Args:
        tide_levels: A list of integers representing tide levels at regular intervals.
                     Constraints: 1 <= len(tide_levels) <= 5*10^3,
                                  0 <= tide_levels[i] <= 10^6.

    Returns:
        An integer representing the number of such moments.

    Examples:
        >>> solution([130, 140, 120, 150, 110, 160])
        1
        >>> solution([100, 160, 150, 130, 140])
        3
        >>> solution([50, 40, 30, 20, 10])
        5
    """
    if not tide_levels:
        return 0

    # The last element is always a dominant reading.
    # We can initialize our count to 1 and the max to the last element.
    count = 1
    max_tide_from_right = tide_levels[-1]

    # Iterate backwards from the second-to-last element to the first.
    for i in range(len(tide_levels) - 2, -1, -1):
        current_tide = tide_levels[i]

        # If the current tide is at least as high as the highest tide
        # seen to its right, it's a "dominant" reading.
        if current_tide >= max_tide_from_right:
            count += 1

        # Update the max tide seen so far from the right.
        max_tide_from_right = max(max_tide_from_right, current_tide)

    return count