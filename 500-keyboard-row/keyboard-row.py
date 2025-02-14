class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = set('qwertyuiop')
        line2 =  set('asdfghjkl')
        line3 =  set('zxcvbnm')

        ans = []

        for word in words:
            w = set(word.lower())

            if w <= line1 or w <= line2 or w <= line3:
                ans.append(word)

        return ans        
