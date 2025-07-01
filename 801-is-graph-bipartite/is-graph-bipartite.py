class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        total = len(graph)
        col = [-1 for i in range(total)]
        isBipartite = True

        for i in range(total):
            if col[i] == -1:
                queue = deque([i])
                col[i] = 0
                while len(queue) > 0:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if col[neighbor] == -1:
                            col[neighbor] = col[node] ^ 1
                            queue.append(neighbor)
                        elif col[neighbor] == col[node]:
                            isBipartite = False
                            break

        return isBipartite
