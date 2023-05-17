inpt = input()
x = 0
y = 0
if(len(inpt)<=20):
    for i in range(len(inpt)):
        if(inpt[i]=='z'):
            x += 1
        elif(inpt[i]=='o'):
            y +=1 
print(x)
print(y)
if ((2*x) == y) :
    print("Yes")
elif(y > (2*x)):
    print("No")
else:
    print("No")
