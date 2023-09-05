class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        t = math.gcd(len(str1), len(str2))
        k = max(len(str1)//t, len(str2)//t)
        
        for i in range(k):
            if (str1[i*t:(i+1)*t] and str1[i*t:(i+1)*t]!=str1[:t]) or (str2[i*t:(i+1)*t] and str2[i*t:(i+1)*t]!=str1[:t]):
                return ""

        return str1[:t]