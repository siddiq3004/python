# def findMedianSortedArrays(nums1,nums2):
#     target = nums2[-1]
#     l , r = 0 , len(nums1)-1
#     op = 0
#     while l <= r:
#         mid = (l+r)//2
#         if target > nums1[mid]:
#             l = mid +1
#         elif target < nums1[mid]:
#             r = mid -1
#         else:
#             pos = l+1
#             break
#         pos = l
#     i=0
#     while i < len(nums2):
#         nums1.insert(pos,nums2[i])
#         pos +=1
#         i +=1
    
#     if len(nums1) % 2 == 0:
#         mid = (l+r)//2
#         op = (nums1[mid] + nums1[mid+1])/2 * 10**-5
#     else:
#         mid = (l+r)//2
#         op = (nums1[mid] + nums1[mid+1])/2 * (10**-5)
#         op = nums1[mid] * (10**-5)
#     return op
# nums1 = [1,3]
# nums2 = [2]
# print(findMedianSortedArrays(nums1,nums2))