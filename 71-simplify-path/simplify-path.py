class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for c in path.split("/"):
            if stack and c == ".." :
                stack.pop()
            elif c != "." and c != "" and c != "..":
                stack.append(c)

        return "/" + "/".join(stack)