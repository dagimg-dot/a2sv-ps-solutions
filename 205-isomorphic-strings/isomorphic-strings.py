class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        _s = []
        _t = []

        for c in s:
            _s.append(s.index(c))
        
        for c in t:
            _t.append(t.index(c))

        return True if _s == _t else False