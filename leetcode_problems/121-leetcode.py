class Solution:
    def maxProfit(self, prices):
        l = 0
        r = 1
        curr_ = 0
        max_ = 0
        for i in range(len(prices)-1):
            if prices[l] <= prices[r]:
                curr_ = (prices[r] - prices[l])
                max_ = max(max_,curr_)
                r +=1
            else:
                l = i+1
                r +=1
        return max_
                