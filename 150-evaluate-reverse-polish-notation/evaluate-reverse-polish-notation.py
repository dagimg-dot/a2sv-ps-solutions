class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+", "-", "*", "/"}

        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                b, a = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    stack.append(int(a / b))
                    
        return stack.pop()