class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        avail = []
        
        for idx in arr2:
            avail.extend([idx] * count[idx])
            count.pop(idx)

        count = dict(sorted(count.items(),key=lambda x:x[0]))

        for key, value in count.items():
            avail.extend([key] * value)

        return avail

            