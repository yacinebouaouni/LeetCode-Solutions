class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1, n2, n3 = len(s1), len(s2), len(s3)
        memo = {}
        
        def recursive(i1,i2,i3):

            if i1==n1 and i2==n2 and i3==n3:
                return True

            if (i1,i2,i3) in memo:
                return memo[(i1,i2,i3)]
            else:
                memo[(i1,i2,i3)] =  i3<n3 and (i1<n1 and s1[i1] == s3[i3] and recursive(i1+1,i2,i3+1) or (i2<n2 and s2[i2]==s3[i3] and recursive(i1,i2+1,i3+1)))
                return memo[(i1,i2,i3)]

        
        return recursive(0,0,0)