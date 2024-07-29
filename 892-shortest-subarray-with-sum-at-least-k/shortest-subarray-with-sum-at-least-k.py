class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        pre_sum = [0]*(n+1)
        
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + A[i-1]
        
        deq = collections.deque([])
        res = float("inf")
        
        for i in range(n+1):
            while deq and pre_sum[i]-pre_sum[deq[0]] >= K:
                res = min(res, i-deq[0])
                deq.popleft()
            while deq and pre_sum[i] <= pre_sum[deq[-1]]:
                deq.pop()
                
            deq.append(i)
            
        return res if res != float("inf") else -1
