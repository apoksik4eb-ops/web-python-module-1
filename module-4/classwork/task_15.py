import random

nums = [random.randint(-50, 50) for _ in range(100)]

def random_list(i, best_pos=0, best_sum=None):
    if i + 10 > len(nums):
        return best_pos
    
    summ = sum(nums[i: i + 10])
    
    if best_sum  == None or summ < best_sum:
        best_sum = summ
        best_pos = i

    return random_list(i + 1, best_pos, best_sum)


best_pos = random_list(0)
print(nums[best_pos: best_pos + 10])



