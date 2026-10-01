class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # approach
        # Use a map. 
        # At each step, check if target - curr ele exists. If not
        # add to map.
        # If we find the pair return pair.

        mp = {}
        res = []
        size = len(nums)
        for i in range(len(nums)):
            if (target - nums[i] in mp):
                res.append(mp[target - nums[i]])
                res.append(i)
            else:
                mp[nums[i]] = i
        return res
             