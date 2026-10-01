class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # method 
        # add elements into a set and then check if it exists/not

        mySet = set()
        for i in range(len(nums)):
            if nums[i] in mySet:
                return True
            else:
                mySet.add(nums[i])
        return False