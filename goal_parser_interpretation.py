class Solution:
    def interpret(self, command: str) -> str:
        l = 0
        ans = ""

        while l < len(command):
            if command[l] == "G":
                ans += "G"
                l += 1
            elif command[l] == "(":
                if l + 1 < len(command) and command[l + 1] == ")":
                    ans += "o"
                    l += 2
                else:
                    ans += "al"
                    l += 4
                    
        return ans