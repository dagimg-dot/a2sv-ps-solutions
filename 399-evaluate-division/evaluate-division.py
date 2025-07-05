class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for (dividend, divisor), weight in zip(equations, values):

            graph[dividend][divisor] = weight
            graph[divisor][dividend] = 1 / weight

        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0

            if src == dest:
                return 1.0

            visited.add(src)

            for neighbor, w in graph[src].items():
                if neighbor in visited:
                    continue

                temp = dfs(neighbor, dest, visited)
                if temp != -1:
                    return temp * w

            return -1

        res = []
        for v1, v2 in queries:

            visited = set()
            res.append(dfs(v1, v2, visited))
        return res
