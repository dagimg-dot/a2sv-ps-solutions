class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1

            return True

        l = 0
        r = len(s) - 1        

        while l < r:
            if s[l] != s[r]:
                x = isPalindrome(s, l + 1, r)
                y = isPalindrome(s, l, r - 1)

                if x or y:
                    return True
                else:
                    return False

            l += 1
            r -= 1

        return True
