from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for i in range(len(arr)):
            count[arr[i]] = count.get(arr[i],0) + 1
        
        maxLucky = 0
        for key,value in count.items():
            if key == value:
                maxLucky = max(maxLucky, key)

        if maxLucky == 0:
            return -1  
        else: 
            return maxLucky  