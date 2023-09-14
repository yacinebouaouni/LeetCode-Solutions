class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left, right = 0, len(nums)-1
        found = 0
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                found = 1
                break

            if nums[mid] < target:
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

        if found == 0:
            return [-1,-1]

        else:
            start = end = mid 
            while start-1 >= 0 and nums[start-1] == target:
                start -= 1
            while end+1 <= len(nums)-1 and nums[end+1] == target:
                end += 1

            return [start, end]
