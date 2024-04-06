from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_freq = {}
        start = words[0]

        for char in start:
            char_freq[char] = char_freq.get(char, 0) + 1

        for i in range(1, len(words)):
            curr_word = words[i]
            char_freq_curr = {}
            for char in curr_word:
                char_freq_curr[char] = char_freq_curr.get(char, 0) + 1

            for char in char_freq.keys():
                if char in char_freq_curr:
                    char_freq[char] = min(char_freq[char], char_freq_curr[char])
                else:
                    char_freq[char] = 0

        common_chars = []
        for k, v in char_freq.items():
            common_chars += [k]*v

        return common_chars