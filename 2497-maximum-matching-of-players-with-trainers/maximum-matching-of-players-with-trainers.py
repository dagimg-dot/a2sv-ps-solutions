class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        match = 0

        i = len(players) - 1
        j = len(trainers) - 1
        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                match += 1
                i -= 1
                j -= 1
            else:
                i -= 1

        
        return match