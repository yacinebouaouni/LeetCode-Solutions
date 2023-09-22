class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        output = float('inf')
        p1 = 0
        currSum = 0
        for p2 in range(len(nums)):
            currSum += nums[p2]
            while currSum >= target:
                output = min(p2-p1+1, output)
                currSum -= nums[p1]
                p1 += 1
                
                
        return output if output != float('inf') else 0