nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    num_indexes = {}
    for i, num in enumerate(nums):
        print(i,num)
        print(num_indexes)
        if target - num in num_indexes:
            print('已经找到了')
            return [num_indexes[target - num], i]
        num_indexes[num] = i
    return []

print(twoSum(nums,target))