class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.minInt = 1


    def popSmallest(self) -> int:
        if not self.heap:
            self.minInt += 1
            return self.minInt-1

        return heapq.heappop(self.heap)
        

    def addBack(self, num: int) -> None:
        if num < self.minInt and num not in self.heap:
            heapq.heappush(self.heap, num)
        

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)