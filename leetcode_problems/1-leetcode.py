# class Solution:
def twoSum(nums, target):
    prev_hashmap = {}  #hashmap
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prev_hashmap:
            return(prev_hashmap[diff],i)
        prev_hashmap[n]=i
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
# li = "RDD"
# list(li)
# print(li)
        