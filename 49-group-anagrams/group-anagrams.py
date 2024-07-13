class Solution:
    def sortWord(self, strs: List[str]) -> List[str]:
        return "".join(sorted(strs))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}

        for i in range(len(strs)):
            w = self.sortWord(strs[i])
            if w in s:
                s[w].append(strs[i])
            else:
                s[w] = [strs[i]]

        return list(s.values())
                