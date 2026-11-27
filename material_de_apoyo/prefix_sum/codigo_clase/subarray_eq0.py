data = [2,3,4,5,6,1,-2,-5,-5]

def subarray_equal_to0(data):
    current_sum = 0
    counter = {0:1}
    for i in data:
        current_sum += i
        print(current_sum)
        cc = counter.get(current_sum, 0)
        if(cc >= 1): 
            return True
        counter[current_sum] = counter.get(current_sum, 0) + 1

    return False

print(subarray_equal_to0(data))
