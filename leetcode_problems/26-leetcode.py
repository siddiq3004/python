# nums = [1,1,2,3,3,4,4,4,6,7]
# l,r = 0,1
# while r<=len(nums)-1:
#     # print(nums[-1])
#     if nums[l] == nums[r]:
#         r +=1
#     else:
#         l +=1
#         nums[l] = nums[r]
#         r +=1
# # for i in range(l,len(nums)):
# #     curr = nums[i]
# #     curr.replace('curr','_')
# # return l
# print(l+1)
def isPalindrome(x):
    y = []
    n = len(x)-1
    x = str(x)
    for i in range(n,-1,-1):
        print(i)
        y[n-i]= x(i)
        # print(int(y))
        print(x)
    if x == y:
        # print('True')
        return True
    return False
x = 121
print(isPalindrome(x))
