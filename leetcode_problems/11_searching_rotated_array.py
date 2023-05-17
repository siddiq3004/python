# class Solution(object):
#     def search(self, nums, target):
#         low = 0
#         count = 0
#         high = len(nums)-1
#         # print(high)
#         # print(type(nums[0]))
#         mid =int((low + high)/2)
#         # print(mid)
#         while low<=high: 
#             if target == nums[mid] :
#                 return mid
#                 # print(mid)
#                 break
#                 # count = 1
#             elif target>nums[mid]:
#                 low = mid+1
#             else:
#                 high = mid-1
#         # if count == 0:
#         #     low = mid+1
#         #     new_mid = (low+high)/2
#         #     while low<=high:
#         #         if nums[new_mid]== target:
#         #             return new_mid
#         #         elif nums[mid]>target:
#         #             low =new_mid+1
#         #         elif nums[mid]<target:
#         #             high = new_mid-1           
                

            





# nums = list(map(int,input()))
# target = 5
# p1 = Solution()
# print(p1.search(nums,target))

# rows = int(input("Enter number of rows: "))

# k = 0
# count=0
# count1=0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print("  ", end="")
#         count+=1
    
#     while k!=((2*i)-1):
#         if count<=rows-1:
#             print(i+k, end=" ")
#             count+=1
#         else:
#             count1+=1
#             print(i+k-(2*count1), end=" ")
#         k += 1
    
# count1 = count = k=0
# print()
M = 5
min = 0
max = 0
A = list(map(int,input().strip().split()))
print(A)
print(type(A))
# A = {5,9,6,4,7,3,2}
A.sort()
print(A)
min = int(A[0])
max = int(A[M-1])
diff = max-min
print(diff)

# A = [2,5,8,1,3]
# A.sort()
# print(A)