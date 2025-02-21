class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n, m = len(image), len(image[0])

        def invertCell(val):
            if val == 0:
                return 1
            else:
                return 0

        for i in range(len(image)):
            image[i] = image[i][::-1]
        
        for i in range(n):
            for j in range(m):
                image[i][j] = invertCell(image[i][j])
                
            
        return image
        