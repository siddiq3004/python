# class Solution(object):
#     def containsDuplicate(self, nums):
#         unique_list = []
#         count = 0
#         self.nums = nums
#         for x in self.nums:
#             if x not in unique_list:
#                 unique_list.append(x)
#             else:
#                 count = 1
#                 print('true')
#                 break

#         if count ==0:
#             print('false')
#             return 0

# nums = list(input())
# p1 = Solution()
# p1.containsDuplicate(nums)

# print(nums)


nums = [1,1,1,3,3,4,3,2,4,2]
print(nums)
# count = 1
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] == nums[j]:
#             count += 1

# if count > 2:
#     print("False")
# else:
#     print('True')
