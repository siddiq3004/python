inpt = list(input())
print(inpt)
print(inpt[0])
count = 0
for i in range(len(inpt)-1):
    if((i+1) % 2 != 0):
        if(inpt[i]=='(' and inpt[i+1]==')'):
            count += 0
        else:
            count+=1
print(count)
