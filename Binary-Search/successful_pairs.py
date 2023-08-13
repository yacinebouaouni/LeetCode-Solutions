class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        M = len(potions)
        output = []

        for s in spells:

            if s * potions[0] >= success:
                output.append(M)
            elif s * potions[-1] < success:
                output.append(0)
            else:
                left, right = 0, M-1
                while left <= right:
                    mid = (left+right)//2
                    if potions[mid] * s >= success and potions[mid-1] * s < success:
                        break
                    if potions[mid] * s >= success and potions[mid-1] * s >= success:
                        right = mid - 1
                    if potions[mid] * s < success:
                        left = mid +1

                output.append(M-mid)


        return output