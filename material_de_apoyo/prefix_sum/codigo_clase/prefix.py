from typing import List
def get_prefix_array(data: List[int]) -> List[int]:
    new_data: List[int] = []
    current_sum: int = 0
    
    for value in data:
        current_sum += value
        new_data.append(current_sum)
        
    return new_data

def get_subarray_sum(prefix_data: List[int], left: int, right: int) -> int:
    if left == 0:
        return prefix_data[right]
    return prefix_data[right] - prefix_data[left-1]    