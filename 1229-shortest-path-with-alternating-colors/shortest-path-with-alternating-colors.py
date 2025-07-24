class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:

        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)

        for x, y in redEdges:
            graph_red[x].append(y)

        for x, y in blueEdges:
            graph_blue[x].append(y)

        ans = [float("inf")] * n
        queue = deque()
        visited = set()

        # current_node, steps, color
        if 0 in graph_red.keys():
            queue.append((0, 0, "red"))
        if 0 in graph_blue.keys():
            queue.append((0, 0, "blue"))

        while queue:
            cur, steps, color = queue.popleft()

            ans[cur] = min(ans[cur], steps)

            if color == "blue":
                for neighbors in graph_blue[cur]:
                    if (neighbors, "red") not in visited:
                        queue.append((neighbors, steps + 1, "red"))
                        visited.add((neighbors, "red"))
            if color == "red":
                for neighbors in graph_red[cur]:
                    if (neighbors, "blue") not in visited:
                        queue.append((neighbors, steps + 1, "blue"))
                        visited.add((neighbors, "blue"))

        for i in range(1, len(ans)):
            if ans[i] == float("inf"):
                ans[i] = -1
        ans[0] = 0

        return ans
