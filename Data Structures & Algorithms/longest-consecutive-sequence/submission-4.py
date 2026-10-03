class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # method -> cant use num + 1 (opp logic I thought of)

        # iterate through the array and check if num -1 exists
        # in set. If no, only then, consider this element as 
        # starting point. 
        # check for max window length by using set to avoid dups
        # o(n), o(n)
        
        my_set = set(nums)
        res = 0

        for i in range(len(nums)):
            if(nums[i] - 1 not in my_set): # window start
                length = 1
                while(length + nums[i] in my_set): 
                    # lookup for set is o(1) so total is o(n)
                    length = length + 1
                res = max(res, length)
        return res
                


