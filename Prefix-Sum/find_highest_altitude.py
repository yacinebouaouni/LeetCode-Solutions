class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        currAtt = maxAtt = 0
         
        for g in gain:
            currAtt += g
            maxAtt = max(currAtt, maxAtt)
        
        return maxAtt