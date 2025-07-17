class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        neg_stones = [-i for i in stones]

        heapq.heapify(neg_stones)
        
        while len(neg_stones) > 1:
            first = -heapq.heappop(neg_stones)
            second = -heapq.heappop(neg_stones)
            if first != second:
                heapq.heappush(neg_stones, -(first - second))
        
        return -neg_stones[0] if neg_stones else 0