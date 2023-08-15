class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        maxLong = start = nZero = 0

        for end in range(len(nums)):
            
            if nums[end] == 0:
                nZero += 1

            while nZero > 1:
                if nums[start] == 0:
                    nZero -= 1
                start += 1
            
            maxLong = max(maxLong, end-start)

        return maxLong