class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        total = sum(nums)
        currSum = 0

        for i in range(len(nums)):

            if total - nums[i] - currSum == currSum:
                return i

            currSum += nums[i]

        return -1

