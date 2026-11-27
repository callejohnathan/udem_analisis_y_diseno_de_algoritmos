data = [2, 7, 4,4]
prefix = [1 if x % 2 == 0 else -1 for x in data]
 
counter = {0:1}
current_sum = 0
counter_ = 0
for i in prefix:
    current_sum += i
    counter_ += counter.get(current_sum, 0)
    counter[current_sum] = counter.get(current_sum, 0) + 1
    
print(counter_)

