class Solution:
    def reverseVowels(self, s: str) -> str:

        left, right = 0, len(s)-1
        output = list(s)
        vowels = set(['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'])

        while left < right:

            if s[left] in vowels and s[right] in vowels:
                output[right], output[left] = output[left], output[right]
                right -= 1
                left += 1

            elif s[right] in vowels:
                left += 1

            elif s[left] in vowels:
                right -= 1

            else:
                right -= 1
                left += 1

        return "".join(output)