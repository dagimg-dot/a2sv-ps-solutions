class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        def findNeighbour(i, j):
            return [img[x][y] for x in (i-1, i, i+1) for y in (j-1, j, j+1) if 0 <= x < m and 0 <= y < n]


        ans = [[0] * len(img[0]) for _ in range(m)]

        for i in range(len(img)):
            for j in range(len(img[0])):
                neighbour = findNeighbour(i, j)
                ans[i][j] = sum(neighbour) // len(neighbour)

        
        return ans

        
