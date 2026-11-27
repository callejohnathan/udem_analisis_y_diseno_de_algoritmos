from typing import List, Dict

def count_subarrays_equal_to_k(arr: List[int], k: int) -> int:
    freq: Dict[int, int] = {0: 1}   # prefix_sum 0 visto una vez (subarreglos que empiezan en 0)
    prefix_sum: int = 0
    count: int = 0

    for x in arr:
        prefix_sum += x #1
        print(freq, prefix_sum - k)
        count += freq.get(prefix_sum - k, 0) 
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

print(count_subarrays_equal_to_k([1,3,2,7,-7,-2,3,1,1], 5))
    