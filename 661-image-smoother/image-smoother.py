class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        def findNeighbour(i, j):
            neighbors = [] 

            for x in range(i-1, i+2):  
                for y in range(j-1, j+2):
                    if 0 <= x < m and 0 <= y < n:
                        neighbors.append(img[x][y])
            
            return neighbors


        ans = [[0] * len(img[0]) for _ in range(m)]

        for i in range(len(img)):
            for j in range(len(img[0])):
                neighbour = findNeighbour(i, j)
                ans[i][j] = sum(neighbour) // len(neighbour)

        
        return ans

        
