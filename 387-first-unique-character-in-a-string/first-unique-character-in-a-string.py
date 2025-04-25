class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for key, value in count.items():
            if value == 1:
                return s.index(key)
            
        return -1
