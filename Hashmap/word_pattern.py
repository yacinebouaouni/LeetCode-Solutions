class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        mapping = dict()
        if len(s)!=len(pattern):
            return False
        if len(set(s)) != len(set(pattern)):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in mapping:
                    mapping[pattern[i]] = s[i]
                elif mapping[pattern[i]] != s[i]:
                    return False

        return True