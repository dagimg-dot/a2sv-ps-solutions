class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = 0
        ans = ""

        while l < len(s):
            r = l + 2
            if r < len(s) and s[r] == "#":
                num = int(s[r - 2] + s[r - 1])
                ans += chr(97 + num - 1)
                l = r + 1
            else:
                ans += chr(97 + int(s[l]) - 1)    
                l += 1

        return ans