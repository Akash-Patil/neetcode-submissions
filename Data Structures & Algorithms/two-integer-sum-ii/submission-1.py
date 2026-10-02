class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # method
        # keep 2 pointers, one a start and 1 at back
        # Till right > left, based on sum at that time, move
        # pointers accordingly

        n = len(numbers)
        left = 0
        right = n-1
        res = []

        while (right > left):
            sum = numbers[left] + numbers[right]
            if(sum > target):
                right = right - 1
            elif(sum < target):
                left = left + 1
            else:
                res.append(left + 1)
                res.append(right + 1)
                return res

        return res