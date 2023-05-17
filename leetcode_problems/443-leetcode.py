chars = ["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]
s = []
count =0
hashmap = {}
for i,n in enumerate(chars):
    if n in hashmap:
        hashmap[n] +=1
    else:
        hashmap[n] = 1
# s.append(chars[0])
for key , val in hashmap.items():
    if hashmap[key] == 1:
        s += (key)
        print('s1',s)
    else:
        s += (key) + (str(val))
        print('s2',s)
        print(type(s))
print(len(s))
# s = []
# s += chars[0]
# print(s)
# s1 ,c1,i,l = 0,1,0,0
# while i < len(chars)-1:
#     if chars[i+1] == s[s1]:
#         c1 +=1
#         i +=1
#         print('c1' , c1)
#     else:
#         print('hi')
#         int_ = []
#         strc = str(c1)
#         print('lenstrc',len(strc))
#         for k in range(len(strc)):
#             int_ += strc[k] 
#             print('int_',int_)
#             s += int_[k]
#             print ('s',s)
#             s1 += k+1
#             print('s1',s1)
#         int_ = None
#         c1 = 1
#         s[s1]=chars[i]
#         i +=1
# print(len(s))
# print(s)