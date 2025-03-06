class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals, key=lambda x:x[0]))

        ans = []

        for interval in intervals:
            if ans and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans += [interval]

        return ans