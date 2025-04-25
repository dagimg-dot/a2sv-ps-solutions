class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def dfs(start):
            sinb = ""
            mul = 0

            while start[0]<n:
                if s[start[0]] == '[':
                    start[0]+=1
                    sinb += mul*dfs(start)
                    mul = 0
                elif s[start[0]] == ']':
                    return sinb
                elif s[start[0]].isdigit():
                    mul = mul*10+int(s[start[0]])
                else:
                    sinb+=s[start[0]]
                start[0]+=1

            return sinb
            
        a = dfs([0])

        return a