s = "((()))"
# print(s[0])
stack = []
closeToOpen = {")":"(","]":"[","}":"{"}
for c in s:
    print(c)
    print ('st',stack)
    print('hii')
    if c in closeToOpen:
        print('cto',closeToOpen[c])
        print('hii')
        print('cto-',closeToOpen)
        if stack and stack[-1] == closeToOpen[c]:
            print ('st',stack)
            stack.pop()
            print ('st',stack)

        else:
            print(False) 
    else:
        stack.append(c)
print(True if not stack else False) 