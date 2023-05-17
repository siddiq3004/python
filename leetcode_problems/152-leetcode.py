class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        curmin , curmax = 1,1
        for n in nums:
            if n==0:
                curmin , curmax = 1,1
                continue
            temp = curmax*n
            curmax = max(n*curmin,n*curmax,n)
            curmin = min(n*curmin,temp,n)
            res = max(res,curmax)
        return res