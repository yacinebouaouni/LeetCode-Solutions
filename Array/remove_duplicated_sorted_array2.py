class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        curr = nums[0]
        count = 1
        index = 1
        for i in range(1, len(nums)):
            if nums[i] == curr and count <= 1:
                count += 1
                nums[index] = nums[i]
                index += 1

            if nums[i] != curr:
                nums[index] = nums[i]
                index += 1
                count = 1
                curr = nums[i]

        return index
