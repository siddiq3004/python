# n = int(input())
# str1 = list(input())
# flag = 0

# for i in range(len(str1) - 1):
#     if(str1[i] == 'H'and str1[i + 1] != '.'):
#         flag = 1
#         print("NO")
#         break;
#     if(str1[i] == "."):
#         str1[i] = 'B'
# if flag == 0:
#     print('YES')
#     if str1[len(str1) - 1] == ".":
#         str1[len(str1) - 1] ='B'
#     print(''.join(map(str,str1)))

a = [1,2]
b = [3,4]
# a = str(a)
a = a +b
# a = list(str(a).split(''))
print(type(a))
print(a)
