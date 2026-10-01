class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# method
# [10, 1, 5, 6, 7, 1]
# keep track of the start -> 10 -> 1
# end of window -> 5 -> 6 
# diff -> 0 (change start), 4, 5, 6, 
# store the diff and max compare if next ele is lesser than equal to start ele.
# max(diff, curr_diff)
        res = 0
        j = 0
        for i in range(len(prices)):
            start = prices[j]
            if(prices[i] >= start):
                curr_diff = prices[i] - start
                res = max(res, curr_diff)
            else:
                j = i
        return res