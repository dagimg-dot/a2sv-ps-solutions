class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_rad = 0
        heaters.sort()

        for i in range(len(houses)):
            l = 0
            r = len(heaters) - 1

            rad = float('inf')

            while l < r:
                mid = l + (r - l) // 2

                if heaters[mid] == houses[i]:
                    rad = 0
                    break
                elif heaters[mid] < houses[i]:
                    rad = min(rad, abs(heaters[mid] - houses[i]))
                    l = mid + 1
                else:
                    rad = min(rad, abs(heaters[mid] - houses[i]))
                    r = mid
            rad = min(rad, abs(heaters[l] - houses[i]))
            max_rad = max(rad, max_rad)
        
        return max_rad