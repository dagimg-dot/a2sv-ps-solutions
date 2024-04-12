class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        open = ['(', '[','{']
        paren = ["()","[]","{}"]

        for p in s:
            if p in open:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                elif (stack[-1] + p) in paren:
                    stack.pop()
                else:
                    return False
        
        return not bool(len(stack))