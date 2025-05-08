class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(letters[-1]) <= ord(target):
            return letters[0]

        for char in letters:
            if ord(char) > ord(target):
                return char