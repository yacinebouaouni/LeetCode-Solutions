class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]
        def bisect(nums, target, findLeft):
            left, right = 0, len(nums)-1
            i = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    i = mid
                    if findLeft:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i


        start, end = bisect(nums,target, True), bisect(nums, target, False)
        return [start, end]

                
