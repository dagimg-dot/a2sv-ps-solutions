class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_of = {}
        
        ans = []
        size, end = 0, 0

        for i in range(len(s)):
            last_of[s[i]] = i

        
        for i in range(len(s)):
            size += 1
            end = max(end, last_of[s[i]])

            if i == end:
                ans.append(size)
                size = 0

        return ans
        
