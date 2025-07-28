class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[0] - x[1]))
        n = len(costs) / 2
        n1 = 0
        n2 = 0
        totalCost = 0

        for c1, c2 in costs:
            if (n1 < n and c1 <= c2) or n2 == n:
                totalCost += c1
                n1 += 1
            else:
                totalCost += c2
                n2 += 1

        return totalCost
