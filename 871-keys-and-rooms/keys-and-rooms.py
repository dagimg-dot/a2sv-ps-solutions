class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = [False] * n
        visited[0] = True
        keys = set()
        for i in rooms[0]:
            keys.add(i)

        while keys:
            temp = set()
            for i in keys:
                if not visited[i]:
                    visited[i] = True
                    for j in rooms[i]:
                        temp.add(j)

            keys = temp

        return all(visited)
