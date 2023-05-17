# product of array except self
class Solution:
    def productExceptSelf(self, nums):
        postfix = 1
        prefix = 1
        l,r = 0,len(nums)
        res = [1]* (len(nums))
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

            res[r-(i+1)] *=postfix
            postfix *= nums[r-(i+1)]
        return res


