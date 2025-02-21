class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)

        ans = 0

        for word in words:
            w_count = Counter(word)

            isValid = True

            for key, value in w_count.items():
                if key not in chars_count or value > chars_count[key]:
                    isValid = False

            if isValid == True:
                ans += len(word)

        
        return ans
                


            


