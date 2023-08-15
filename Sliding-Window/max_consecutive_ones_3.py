class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        currMax = 0
        nZero = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                nZero += 1

            while nZero > k:
                if nums[start] == 0:
                    nZero -= 1
                start += 1

            currMax = max(currMax, end - start + 1)

        return currMax
