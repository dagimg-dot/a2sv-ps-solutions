class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles: 
                hours += ceil(bananas / k)
            
            return hours <= h
        
        l = 1
        r = max(piles)

        while l <= r:
            mid = l + (r - l) // 2

            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
            
        return l
        