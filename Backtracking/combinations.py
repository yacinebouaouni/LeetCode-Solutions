class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        def backtrack(comb, start):

            if len(comb) == k:
                ans.append(comb[:])
                return
            # If there are not enough remaining elements to form a valid combination of length 'k', return early.
            if len(comb) + (n - start + 1) < k:
                return

            for i in range(start, n+1):
                comb.append(i)
                backtrack(comb, i+1)
                comb.pop()

        ans = []
        backtrack([], 1)
        return ans