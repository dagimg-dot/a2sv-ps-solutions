class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        match = 0

        i = 0
        j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                match +=1
                i += 1
                j += 1
            else:
                i += 1
            
        return match
