nums = [-2,1,-3,4,-1,2,1,-5,4]
fi = 0
li = len(nums)-1
print(li)
for i in nums[:]:
    
    if i >0:
        print('i',fi)
        break
    else:
        fi+=1
for j in nums[::-1]:
    # print('j :',j)

    if j >0:
        print('li :',li)
        break
    else:
        li -=1
new_num =nums[(fi):(li)+1]
print(new_num)
# for i in range(len(new_num)):
#     if 
# for i in range(len(new_num)):
#     sum_total = sum(new_num)
#     min_val = min(new_num)
#     if 
