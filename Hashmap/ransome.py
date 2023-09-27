class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        for char in ransomNote:
            if magazine[char] == 0:
                return False
            magazine[char] -= 1
        return True
        