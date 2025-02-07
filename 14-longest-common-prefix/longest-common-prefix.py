class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for i in range(len(common)):
            for string in strs[1:]:
                if i >= len(string) or string[i] != common[i]:
                    return common[:i]

        return common