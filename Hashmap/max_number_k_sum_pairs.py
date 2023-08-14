class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        hashmap = defaultdict(int)
        count = 0
        for num in nums:

            if num in hashmap and hashmap[num] > 0:
                count += 1
                hashmap[num] -= 1

            elif num < k:
                hashmap[k-num] += 1
            
        return count