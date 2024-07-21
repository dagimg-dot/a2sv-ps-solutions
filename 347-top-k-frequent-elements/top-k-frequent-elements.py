class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
        print(sorted_count)
        result = list(sorted_count.keys())[:k]
        return result