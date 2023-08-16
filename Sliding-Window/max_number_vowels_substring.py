class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a','e','i','o','u'}
        currMax = 0
        for i in range(k):
            if s[i] in vowels:
                currMax += 1
        
        currNum = currMax
        for end in range(k, len(s)):

            currNum = currNum + (s[end] in vowels) - (s[end-k] in vowels)
            currMax = max(currMax, currNum)
        
        return currMax

