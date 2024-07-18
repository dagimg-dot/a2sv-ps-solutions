class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        d = {}
        _long = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1

            count = r - l + 1
            if (count - max(d.values())) <= k:
                _long = max(_long, count)
            else:
                d[s[l]] -= 1
                if not d[s[l]]:
                    d.pop(s[l])
                l += 1
            
        
        return _long
