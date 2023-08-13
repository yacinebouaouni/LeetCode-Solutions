class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def total_hours(k):
            return sum([math.ceil(pile/k) for pile in piles])


        left, right = 1, max(piles)
        k = right
        while left <= right:

            mid = (left+right)//2

            if total_hours(mid) <= h:
                k = min(k, mid)
                right = mid - 1

            else:
                left = mid + 1 

        return k