# T = int(input())
# for i in range(T):
#     array = int(input())
#     arr = list(map(int,input().strip().split()))[:array]
#     print(arr)
#     count = 0
#     for i in range(1,len(arr)+1):
#         for j in range(1,len(arr)+1):
            
#             if c <= (array) :

#                 if (arr[c] ^ arr[j]) == (arr[j] ^arr[c]) :
#                     print(arr[c],arr[j])




#             if arr[i]<arr[j]:
#                 c = arr[i]
#                 if c < (array-1) :

#                     if (arr[c] ^ arr[j]) == (arr[j] ^arr[c]) :
#                         print(arr[c],arr[j])
#                         count +=1
#     print(count)


# T = int(input())
# for i in range(T):
#     array = int(input())
#     arr = list(map(int,input().strip().split()))[:array]
#     print(arr)
#     count = 0
#     for i in range(1,len(arr)):
#         for j in range(1,len(arr)): 
#             c = arr[i-1]
#             if (c <= (array-1)) :

#                 if (arr[c] ^ arr[j-1]) == (arr[j-1] ^arr[c]) :
#                     print(arr[c],arr[j-1])
#             if 0<arr[i-1]<arr[j-1]<array:
#                 count +=1
#     print(count)
    
T = int(input())
for i in range(T):
    array = int(input())
    arr = list(map(int,input().strip().split()))[:array]
    count = 0
    for i in range(1,array+1):
        for j in range(1,array+1):
            if(arr[i-1]<=arr[j-1]):
                if (arr[i-1] ^ j) == (arr[j-1] ^ i) :
                    count +=1
    print(count)