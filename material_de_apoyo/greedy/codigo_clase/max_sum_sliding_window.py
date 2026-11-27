from typing import List
data = [5,200,-1,0,30,15,-2,-7,-8]
k = 3

def max_sum_sliding_window(nums: List[int], k: int) -> int:
    if(len(nums) < k): return 0
    window_sum: int = sum(data[:k])
    max_sum: int = window_sum
    for i in range(len(nums)-k):
        window_sum = window_sum - nums[i] + nums[i+k]
        max_sum = max(window_sum, max_sum)
    return max_sum

print(max_sum_sliding_window(data, 3))
            
    