from typing import List, Any
def first_ocurrence(arr: List[int], element: int) -> int: 
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == element:
            result = mid
            high = mid - 1  # Continue searching in the left half
        elif arr[mid] < element:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return result

# Example usage:
if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3, 3,3,4,4,4,4]
    element = 4
    print(first_ocurrence(arr, element))  # Output: 1