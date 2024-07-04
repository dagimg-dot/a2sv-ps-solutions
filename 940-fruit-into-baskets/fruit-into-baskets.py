class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        count = defaultdict(int)
        
        while r < len(fruits):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res