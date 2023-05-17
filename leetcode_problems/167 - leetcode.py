# def twoSum( numbers, target):
#         dic={}
#         for key,val in enumerate(numbers):
#             if val in dic:
#                 return dic[val],key+1
#             else:
#                 dic[target-val]=key+1
# numbers = [2,3,7,11,15]
# target = 10
# print(twoSum(numbers,target))
# --------------------------------------------
# def addDigits(num: int):
        # length = len(num)
        # Total = 0
        # num = [int(x) for x in str(num)]
        
        # def add(num):
            
#         if num >= 10:
#             output = (num // 10) + (num % 10)
#             return addDigits(output)   
#         else:
#             output = num
#         return output
# num = 38
# print(addDigits(num))
# ------------------------------------
# def bulbSwitch(n) :
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    # op = [1]*n
#     count = 0
#     q = 1
#     while q < n:
#         op[q] = 0
#         q += 2
#     # for i in range(2,n):
#     def iterator(i,j):
#         while j < n :
#             if op[j] == 0:
#                 op[j] = 1
#             else:
#                 op[j] = 0
#             j += (i+1)
#         if i+1 < n:
#             iterator(i+1,i+1)
#     i = 2
#     j = i
#     iterator(i,i)
        
#     for i in range(n):
#         if op[i] == 1:
#             count += 1
#     return count
# print(bulbSwitch(4))

def check(player1):
    p1 , p2 = 1,0
    total = player1[0]
    count = 0
    l1 = len(player1)
    while p1 < l1 :
        if player1[p2] == 10 or count == 2:
            total += player1[p1]
            count = 0
            p2 +=1
        elif player1[p2] == 10:
            total += (2*player1[p1])
            count +=1
        else:    
            total += player1[p1]
            p2 +=1
            
        p1 +=1
        if count >2:
            p2 = p1
    return total
player1 = [7,6,6,3,9,7,5,9,5,9,1,0,0,4,3,1,2]
player2 = [5,0,7,10,4,1,4,2,4,0,1,5,0,10,9,0,4]

check(player1)
print(check(player2))
if check(player1) > check(player2):
    print(1)
elif check(player1) < check(player2):
    print(2)
else:
    print(0)
