class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        prefix = strs[0][:min_len]

        for i in range(1, len(strs)):
            while prefix != strs[i][:len(prefix)]:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
