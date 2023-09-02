class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        heapLeft = costs[:candidates] 
        heapRight = costs[max(candidates, len(costs)-candidates):]
        
        heapq.heapify(heapLeft)
        heapq.heapify(heapRight)
        left, right = candidates, len(costs)-candidates-1
        total = 0

        for _ in range(k):

            if not heapRight or (heapLeft and heapLeft[0] <= heapRight[0]):
                total += heapq.heappop(heapLeft)
                if left <= right:
                    heapq.heappush(heapLeft, costs[left])
                    left += 1

            else:
                total += heapq.heappop(heapRight)
                if left <= right:
                    heapq.heappush(heapRight, costs[right])
                    right -= 1



        return total