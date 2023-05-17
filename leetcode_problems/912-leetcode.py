class Solution:
    def sortArray(self, nums):
        # print('len',len(nums))
        if len(nums)>1:
            print(len(nums)//2)
            left = nums[:len(nums)//2]
            print('l',left)
            right = nums[len(nums)//2:]
            print('r',right)

            # print('right',right)
            # print('lsleft',left)
            # print('lsright',right)
            self.sortArray(left)
            
            
            # print('left',left)
           
            self.sortArray(right)
            # print('rsleft',left)
            # print('rsright',right)
            # print('right',right)
            i,j,k = 0,0,0
            while i<len(left) and j<len(right):
                # print('lf',len(left))
                # print('rf',len(right))
                # print('nums2',nums)
                if left[i] <= right[i]:
                    nums[k] = left[i]
                    
                    i+=1
                    # print('nums1',nums)
                else:
                    # print('nums2',nums)
                    nums[k] = right[j]
                    j+=1
                    # print('nums2',nums)
                k+=1
            while i<len(left):
                # print('nums1',nums)
                nums[k] = left[i]
                # print('nums1',nums)
                i+=1
                k+=1
            while j<len(right):
                nums[k] = right[j]
                # print('nums2',nums)
                j+=1
                k+=1
        return nums
nums = [5,2,3,1]
p = Solution()
p.sortArray(nums)
# sortArray(nums)
print(nums)