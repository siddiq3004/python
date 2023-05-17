needle = "sad"
haystack = "butsad"
a,c = 0 , 0
l =0
i =0 
while i < len(haystack):
    if c < len(needle):
        if needle[c] == haystack[i]:
            c +=1
            if c == len(needle):
                l = c
                break
            i +=1
        else:
            c = 0
            a +=1
            i = a
    else:
        c = 0
        i +=1
print (a if l!=0 else -1)