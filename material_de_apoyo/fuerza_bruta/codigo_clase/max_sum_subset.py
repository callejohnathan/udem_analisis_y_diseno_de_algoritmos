data = [-2, 3, -4, 5, 6]
def max_sum_subset(data):
    subsets = [[]]
    max_subset_sum = 0
    max_subset = []
    for i in data: 
        for j in range(len(subsets)):
            current = subsets[j] + [i]
            current_sum = sum(current)
            if(current_sum > max_subset_sum):
                max_subset_sum = current_sum
                max_subset = current
            subsets.append(current)
                
    return max_subset_sum, max_subset