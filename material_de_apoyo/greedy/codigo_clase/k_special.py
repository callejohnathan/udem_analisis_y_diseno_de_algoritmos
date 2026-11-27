import heapq
from typing import List, Tuple

def mint_to_make_kspecial(string: str, k: int):
    counter: int = 0
    n: int = len(string)
    freqs: dict[str, int] = {}
    #freqs
    for char in string:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    
    #heapify 
    freq_values: List[Tuple[int, str]] = []
    for key, value in freqs.items():
        heapq.heappush_max(freq_values, (value, key))       
    
    ys = [[abs(freq_values[i][0] - freq_values[j][0]) for i in range(len(freq_values))] for j in range(len(freq_values))]
    print(ys)
    return freq_values

data = mint_to_make_kspecial("aabbcccccckkkckckckckkc", 2)
print("X")
print(heapq.heappop_max(data))
print(heapq.heappop_max(data))
print(heapq.heappop_max(data))
print(heapq.heappop_max(data))