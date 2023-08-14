class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointerTarget = 0
        for char in t:

            if pointerTarget >= len(s):
                break
            if char == s[pointerTarget]:
                pointerTarget += 1

        return (pointerTarget >= len(s))