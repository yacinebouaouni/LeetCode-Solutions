class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        output = []
        prefix = ""

        for c in searchWord:
            prefix += c
            tmp = [p for p in products if p.startswith(prefix)]
            output.append(tmp[:min(len(tmp), 3)])
        return output
