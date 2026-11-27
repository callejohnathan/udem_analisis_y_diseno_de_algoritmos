from typing import List
def sum_dig(k: int, m: int, depth: int = 0, current: int = 0, current_sum: int = 0, solutions: List[int] = []) -> List[int]:
    if(current_sum > m):
        return solutions
    if(current != 0):
        solutions.append(current)
    
    for num in range(1,k+1):
        current += num * (10 ** depth)
        current_sum += num 
        sum_dig(k, m, depth+1, current, current_sum)
        current -= num * (10 ** depth)
        current_sum -= num 
        
    return solutions

print(sum_dig(2, 3))
