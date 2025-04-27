class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                new = stack.pop()
                hmap[new] = num
            stack.append(num)
            
        for num in stack:
            hmap[num] =- 1
        
        return [hmap[i] for i in nums1]