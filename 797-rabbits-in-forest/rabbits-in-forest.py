class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        count = Counter(answers)  

        for i,j in count.items():
            if j>i+1:    
                temp = ceil(j/(i+1))
                ans += temp*(i+1)
            else:
                ans+= i+1

        return ans