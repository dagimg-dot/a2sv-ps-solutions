class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")

        def compare(x):
            return int(x[-1])
        
        sorted_words = sorted(words,key=compare)

        return " ".join([w[:-1] for w in sorted_words])