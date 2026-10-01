class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort -> Keep the freq array index as count and
        # array element as list of numbers that have that 
        # particular count as represented by the array index.

        # Use a mp to keep count of the freq of elements
        # Create buckets in freq array
        # As per k, pop out elements and add to the res array
        # o(n), o(n)
        
        mp = {}
        res = []
        for i in range(len(nums)): # count of elements map
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for n,c in mp.items(): # freq list
            freq[c].append(n)
        
        # return res
        for i in range(len(freq) - 1, 0, -1): # from reverse
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
            
