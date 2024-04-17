from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new_list = list(map(str, nums))
        new_list.sort(key=lambda x: x*10, reverse=True)
        final = ''.join(new_list)
        if final[0] == '0':
            return '0'
        else:
            return final
