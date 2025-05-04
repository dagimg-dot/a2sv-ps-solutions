class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()

        for i,c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        nr = len(senate)

        while r and d:
            one = r.popleft()
            two = d.popleft()
            if one < two:
                r.append(nr)
                nr += 1
            else:
                d.append(nr)
                nr += 1

        return 'Radiant' if r else 'Dire'