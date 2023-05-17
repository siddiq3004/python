# class Solution:
#     def canFinish(self, numCourses, prerequisites):
#         # map each course to prereq list
#         preMap = {i:[] for i in range(numCourses)}
#         for crs,pre in prerequisites:
#             preMap[crs].append(pre)
        
#         # visitSet  = all courses along the curr dfs path
#         visitSet = set()
#         def dfs(crs):
#             if crs in visitSet:
#                 return False
#             if preMap[crs]==[]:
#                 return True
#             visitSet.add(crs)
#             for pre in preMap[crs]:
#                 if not dfs(pre):return False
#             visitSet.remove(crs)
#             preMap[crs] = []
#             return True 
#         for crs in range(numCourses):
#             if not dfs(crs):return False
#         return True
# p1 = Solution()
# p1.canFinish(2,[[0,1]])

dict_ = {}
dict_[(1, 23)] = 34
print(dict_)