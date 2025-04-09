class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels_idx = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1} 
        count = 0
        last_reset = -1

        for i in range(len(word)):
            if word[i] not in vowels_idx:
                last_reset = i
                for key in vowels_idx.keys():
                    vowels_idx[key] = -1
                continue

            vowels_idx[word[i]] = i

            min_idx = min(vowels_idx[key] for key in vowels_idx if key != word[i])

            if min_idx == -1:
                continue
            
            count += min_idx - last_reset

        return count
            