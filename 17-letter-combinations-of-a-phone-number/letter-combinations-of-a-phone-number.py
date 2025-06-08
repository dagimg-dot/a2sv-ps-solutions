class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = [""]

        for d in digits:
            new = []
            for s in ans:
                for ch in chars[d]:
                    new.append(s + ch)
            ans = new
            
        return ans if ans[0] != "" else []
