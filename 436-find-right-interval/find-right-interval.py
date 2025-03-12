class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binary_search(intervals, target):
            left = 0
            right = len(intervals) - 1
            while left <= right:
                mid = left + (right-left)//2
                if intervals[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(intervals):
                return -1
            else:
                return left

        hash_map={}

        for idx, interval in enumerate(intervals):
            hash_map[interval[0]]=idx

        intervals.sort()

        res = [-1] * len(intervals)

        for i in range(len(intervals)):
            idx2 = binary_search(intervals, intervals[i][1])
            if idx2 != -1:
                res[hash_map[intervals[i][0]]] = hash_map[intervals[idx2][0]]
            else:
                res[hash_map[intervals[i][0]]] = -1

        return res