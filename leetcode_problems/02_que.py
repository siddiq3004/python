N = int(input())
res = list(map(str,input().strip().split()))[:N]
list1 = []
print(res)
for i in range(N):
    chr = list(res[i])
    list1.append(chr[-1])
print(list1)
op = " ".join(list1)


print(type(op))
print(op)
if(op[-1]=='0'):
    print("YES")
else:
    print("NO")

# def func(list1):
#    while(len(list1) > 2):
#      k=list1[0]
#      for i in list1:
#        if k<i:
#          k=i
#      list1. remove (k)
#      j=list1[0]
#      for i in list1:
#        if j>i:
#          j=i
#      list1.remove(j)
#    return list1
# list2=func([1, 4, 3, 6,5,3,7,8,9,4])
# print(sum (list2)/len(list2))
