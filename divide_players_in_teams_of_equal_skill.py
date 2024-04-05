from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot_sum = skill[0] + skill[-1]
        l = 1
        r = len(skill) - 2
        elist = [skill[0] * skill[-1]]
        while l < r and r < len(skill):
            curr_sum = skill[l] + skill[r]
            if curr_sum != tot_sum:
                return -1
            elist.append(skill[l] * skill[r])
            l += 1
            r -= 1

        return sum(elist)
