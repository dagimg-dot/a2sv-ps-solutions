class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(weights, days, mid):
            count = 0
            day = 0
            for weight in weights:
                if count + weight > mid:
                    count = weight
                    day += 1
                else:
                    count += weight
            return day < days 

        low = max(weights)
        high = sum(weights)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if is_possible(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans