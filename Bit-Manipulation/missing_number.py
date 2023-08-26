class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor = 0
        for n in nums:
            xor ^= n

        for i in range(len(nums)+1):
            xor ^= i

        return xor