class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        result = []
        balls = {}
        colors = defaultdict(set)

        for ball, color in queries:
            if ball in balls:
                prev_color = balls[ball]
                colors[prev_color].discard(ball)
                if not colors[prev_color]: 
                    del colors[prev_color]

            colors[color].add(ball)
            balls[ball] = color

            result.append(len(colors))

        return result