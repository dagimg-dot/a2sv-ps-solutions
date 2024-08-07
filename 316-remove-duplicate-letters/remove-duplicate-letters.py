class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_last_occ_idx_map = {}
        for i in range(len(s)):
            char_last_occ_idx_map[s[i]] = i

        stack = []
        seen = set() 
        for i in range(len(s)):
            if s[i] in seen:
                continue

            while stack and stack[-1] > s[i] and char_last_occ_idx_map[stack[-1]] > i :
                seen.remove(stack[-1])
                stack.pop() 
                
            if s[i] not in seen:
                stack.append(s[i])
                seen.add(s[i])
        
        return ''.join(stack)