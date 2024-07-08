class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        sp = set(spaces)
        new = ""
        while i < len(s):
            if i in sp:
                new += " " + s[i]
            else:
                new += s[i]

            i += 1
        
        return new

        
                        