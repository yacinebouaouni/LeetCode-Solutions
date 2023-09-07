class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        top = max(candies)
        for i, candy in enumerate(candies):
            
            candies[i] = (candy+extraCandies)>=top

        return candies

        