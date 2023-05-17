def romanToInt(s):
    s1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    c =0
    l = 1
    s = list(s)
    n = len(s)
    while l<n:
        if s1[s[l]] <=s1[s[l-1]] :
            c +=s1[s[l-1]] 
            l +=1
            if l == n:
                c +=s1[s[l-1]]
        else:
            c += (s1[s[l]]- s1[s[l-1]])
            if l+2 <= n:
                l = l+2
            else:
                l +=1
    return c
s = "MDCXCV"
print(romanToInt(s))