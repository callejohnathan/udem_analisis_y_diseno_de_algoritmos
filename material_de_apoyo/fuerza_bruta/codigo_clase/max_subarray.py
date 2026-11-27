def max_subarray(nums):
    if(len(nums) == 0): return []
    max_sum = nums[0]
    max_array = [nums[0]]
    for i in range(len(nums)):
        current_array = [nums[i]]
        current_sum = nums[i]
        for j in range(i+1, len(nums)):
            current_array += [nums[j]]
            current_sum += nums[j]
            if(current_sum > max_sum):
                max_sum = current_sum
                max_array = current_array
    return max_sum, max_array

print(max_subarray([1,2,3,4,-50,6]))