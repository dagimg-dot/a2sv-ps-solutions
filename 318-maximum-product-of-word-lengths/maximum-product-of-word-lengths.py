class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0

        for i in range(len(words)):
            for j in range(i,len(words)):
                if not set(words[i]) & set(words[j]):
                    ans = max(ans,len(words[i])*len(words[j]) )

        return ans