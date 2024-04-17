from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        for match in matches:
            win[match[0]] = win.get(match[0], 0)+1
            lose[match[1]] = lose.get(match[1], 0)+1

        no_lost = []
        one_lost = []

        for winner in win.keys():
            if winner not in lose.keys():
                no_lost.append(winner)

        for loser in lose.keys():
            if lose[loser] == 1:
                one_lost.append(loser)

        return [sorted(no_lost), sorted(one_lost)]
