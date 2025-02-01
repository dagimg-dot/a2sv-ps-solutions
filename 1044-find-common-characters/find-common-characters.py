class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        start = words[0]
        char_freq = Counter(start)

        for i in range(1, len(words)):
            curr_word = words[i]
            word_freq = Counter(curr_word)

            for char in char_freq.keys():
                if char in word_freq:
                    char_freq[char] = min(char_freq[char], word_freq[char])
                else:
                    char_freq[char] = 0

        common_chars = []
        for k, v in char_freq.items():
            common_chars += [k] * v

        return common_chars
