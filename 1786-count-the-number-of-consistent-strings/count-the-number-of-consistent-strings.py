class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        
        def isThere(word):
            for i in range(len(word)):
                if word[i] not in allowed:
                    return False

            return True

        for i in range(len(words)):
            count = Counter(words[i])
            word = list(count.keys())
            
            if isThere(word):
                consistent += 1


        return consistent