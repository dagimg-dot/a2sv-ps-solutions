class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos = [p for p in nums if p > 0]
        # neg = [n for n in nums if n < 0]

        # ans = []

        # for i in range(len(pos)):
        #     ans.append(pos[i])
        #     ans.append(neg[i])

        # # return ans

        even_ptr = 0 
        odd_ptr = 1 
        
        result = [0] * len(nums)
        
        for num in nums:
            if num > 0:  
                result[even_ptr] = num
                even_ptr += 2
            else:  
                result[odd_ptr] = num
                odd_ptr += 2  
        
        return result


        

