class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        
        times = []
        idx = 0
        
        for i in range(len(tasks)):
            total_time = processorTime[idx] + tasks[i]
            times.append(total_time)
            
            if (i + 1) % 4 == 0:
                idx += 1
        
        return max(times)