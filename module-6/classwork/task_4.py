nums = (1,2,3,12,13,14,15,123,234,345,456,567)
count = {}

for num in nums:
    len_num = len(str(abs(num)))
    if len_num in count:
        count[len_num] += 1
    else:
        count[len_num] = 1

for key, valius in count.items():
    print(f"{key} = {valius}")