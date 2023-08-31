class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i=j=0
        output = []
        while i<len(word1) and j<len(word2):
            if (i+j)%2 == 0:
                output.append(word1[i])
                i+=1
            else:
                output.append(word2[j])
                j+=1

        if i < len(word1):
            return "".join(output)+word1[i:]
        else:
            return "".join(output)+word2[j:]

