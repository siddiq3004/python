# def isIsomorphic(s,t) :
#         print(len(set(zip(s,t))))
#         return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
# s = 'defhduh'
# t = 'abc'
# print(len(s))
# print(isIsomorphic(s,t))
import collections
from collections import Counter
def longestPalindrome(s):
    ans = 0
    print(Counter(s))
   
    for v in collections.Counter(s).values():
        
        print('v',v)
        ans += v // 2 * 2
        print(ans)
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans
s = 'abccccdd'
print(longestPalindrome(s))














# def find():
#     a = '11'
#     b = '1'
#     carry = 0
#     result = ''
#     i = len(a) - 1
#     j = len(b) - 1
    
#     while i >= 0 or j >= 0 or carry != 0:
#         sum = carry
        
#         if i >= 0:
#             sum += int(a[i])
#             i -= 1
            
#         if j >= 0:
#             sum += int(b[j])
#             j -= 1
            
#         result = str(sum % 2) + result
#         print(result)
#         carry = sum // 2
#         print(carry)
    
#     return result





    # digits = [7,3,9]
    # n = len(digits)
    # for i in range(n-1, -1, -1):
    #     if digits[i] == 9:
    #         digits[i] = 0
    #     else:
    #         digits[i] += 1
    #         return digits
    # print(digits)
    # digits.insert(0, 1)
    # return digits
# print(find())

# str1 = ''
# li = []
# for i in digits:
#     str1 += str(i)
# print(str1)
# print(type(str1[0]))
# str1 = int(str1)
# print(type(str1))

# str1 +=1
# li.append(str1)
# print(li)
# print(type(li))

# digits = int(str1)
# digits +=1
# list(digits)
# print(digits)
# digits = int(digits)
# digits +=1
# list(str(digits))





# def makeConnected(n, connections):
#     li = []
#     count = 0
#     sum_ = 0
#     length = len(connections)+1
#     if (length)<n:
#         return -1
#     else:
#         for i,n in enumerate(connections):
#             print(n[0])
#             if n[0] not in li:

#                 li.append(n[0])
#                 print('li',li)
#                 count +=1
#                 print('c1',count)
#             if n[1] not in li:
#                 li.append(n[1])
#                 print('li',li)
#                 count +=1
#                 print('c2',count)

#         diff = length - count
#         print('diff',diff)

#         sum_ = diff + count
#         print(sum_)
#         print('diff',diff)
#         if (sum_ != n):
#             return diff
#         return -1
# n = 4
# connections = [[0,1],[0,2],[1,2]]
# print(makeConnected(n, connections))
