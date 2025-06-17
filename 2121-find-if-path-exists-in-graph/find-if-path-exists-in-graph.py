class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adjList = defaultdict(list)

        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        visited = set([source])
        stack = [source]

        while stack:
            s = stack.pop()
            if s == destination:
                return True
            else:
                for neighbor in adjList[s]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
                        
        return False
