class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        
        if k == len(nums):
            return currSum/k
        
        maxSum = currSum
        for end in range(k, len(nums)):
            currSum += nums[end]-nums[end-k]
            maxSum = max(maxSum, currSum)
            
        return maxSum/k


