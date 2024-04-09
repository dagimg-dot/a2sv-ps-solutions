class Solution: 
    def select(self, arr, i):
        # code here 
        small = i
        for j in range(i, len(arr)):
            if arr[j] < arr[small]:
                small = j
                
        return small
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,n):
            smallest = self.select(arr, i)
            arr[i], arr[smallest] = arr[smallest], arr[i]
        
        return arr


x = Solution()

y = x.selectionSort([4,1,3,9,7],5)
print(y)