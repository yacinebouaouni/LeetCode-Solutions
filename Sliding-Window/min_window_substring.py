class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = Counter(t)
        p1 = 0
        currLen = float('inf')
        output = ""
        counter = len(table)

        for p2 in range(len(s)):
            if s[p2] in table:
                table[s[p2]] -= 1
                if table[s[p2]] == 0:
                    counter -= 1

            while counter == 0:
                
                if p2-p1+1 < currLen:
                    currLen = p2-p1+1
                    output = s[p1:p2+1]

                if s[p1] in table:
                    table[s[p1]] += 1
                    if table[s[p1]]>0:
                        counter += 1

                p1 += 1
                
        return output