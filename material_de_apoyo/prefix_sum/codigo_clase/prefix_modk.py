from typing import List, Dict

def count_subarrays_modk(array: List[int], k: int) -> int:
    if k == 0:
        raise ValueError("k no puede ser 0")

    remainder_freq: Dict[int, int] = {0: 1}
    current_sum: int = 0
    counter: int = 0

    for value in array:
        current_sum += value
        remainder: int = current_sum % k
        counter += remainder_freq.get(remainder, 0)
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

    return counter

print(count_subarrays_modk([1,3,4,5], 7))