N = int(input())
A = list(map(str,input().strip().split()))[:N]
B = list(map(str,input().strip().split()))[:N]
print(A)
print(B)
sum_A = 0
sum_B = 0
count_A = 0
count_B = 0
no_chng_A = 0
no_chng_B = 0

for i in range(len(A)):
    if(int(A[i])>=0):
        sum_A += int(A[i])
    
    else:
        count_A += 1 
        
	

for i in range(len(B)):
    if(int(B[i])>=0):
        sum_B +=int(B[i])
    else:
        count_B += 1
     
	

if(sum_A >= sum_B):
    diff = sum_A - sum_B
    no_chng_A = 1

else:
    diff = sum_B - sum_A
    no_chng_B = 1



if(count_A == count_B):
    print('Infinite')
elif(0< count_A <= 2 and no_chng_A==1):
    # print(diff+1)
    print(0)
elif(0< count_B <= 2 and no_chng_B==1):
    # print(diff+1)
    print(0)
elif(count_A == 2 or count_B== 2):
    print(diff+1)
    # print(0)
elif(count_A==1 or count_B==1):
    print(1)