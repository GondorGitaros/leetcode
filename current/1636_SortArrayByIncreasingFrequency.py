nums = [1,1,2,2,2,3]

def frequencySort(nums):
    hm = {}
    for i in range(len(nums)):
        if nums[i] in hm:
            hm[nums[i]] += 1
        else:
            hm[nums[i]] = 1
    
    sort_val = sorted(hm.values())
    sort_key = sorted(hm.keys())
    reversed_sort_key = []
    for i in range(len(sort_key) -1, -1, -1):
        reversed_sort_key.append(sort_key[i])
    print(sort_val, reversed_sort_key)
    return_list = []
    for i in range(len(sort_val)):
        for j in range(sort_val[i]):
            return_list.append(reversed_sort_key[len(sort_val) -1 -i])
    return return_list
        
        
print(frequencySort(nums))