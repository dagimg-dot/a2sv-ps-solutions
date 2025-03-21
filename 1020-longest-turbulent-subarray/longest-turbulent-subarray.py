class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        l, max_len = 1, 1
        flag = 0

        for i in range(len(arr) - 1):
            if (flag == 0 or flag == 2) and arr[i] > arr[i + 1]:
                flag = 1
                l += 1
                max_len = max(max_len, l)
            elif (flag == 0 or flag == 1) and arr[i] < arr[i + 1]:
                flag = 2
                l += 1
                max_len = max(max_len, l)
            else:
                if arr[i] == arr[i + 1]:
                    l = 1
                else:
                    l = 2
            
        
        return max_len