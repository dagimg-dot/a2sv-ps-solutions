class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0 
        r = len(s) - 1

        v = ['a','e','i','o','u', 'A', 'E', 'I', 'O','U']

        sl = list(s)

        while l < r:
            if sl[l] in v and sl[r] in v:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
            elif sl[l] in v and sl[r] not in v:
                r -= 1
            elif sl[r] in v and sl[l] not in v:
                l += 1
            else:
                l += 1
                r -= 1
        
        return "".join(sl)