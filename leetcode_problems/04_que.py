t = int(input())
for i in range(t):
    inp = list(map(str,input().strip().split()))[:2]
    n = int(inp[0])
    m = int(inp[1])
    matrix = []
    count = 0
    list1 = []
    
    for i in range(n):
        m = int(inp[1])
        if i==0:
            print("r1 :")
        else:
            print("r2 :")
        # x = list(map(str,input().strip().split()))[:m]
        x = input()
        x = list(x)

        
        # if i==0:
        #     print("r1 :")
        # else:
        #     print("r2 :")
        # a = []
        # for j in range(m):
            
        #     a.append(input())
        matrix.append(x)

    print("printing matrix :",matrix)
    print("----------------------------")
    


    for i in range(n):
        for j in range(m):
            if(matrix[i][j]=='#'):
                count+=1
            else:
                list1.append(count)
                count = 0
    print(list1)

    maxop =0
    for i in range(len(list1)):
        if(list1[i]>= maxop ):
            maxop = list1[i]
        else:
            continue
    print(maxop)

    