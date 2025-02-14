class Solution:
    def maskPII(self, s: str) -> str:
        at_sym = s.find('@')

        # Email
        if at_sym >= 0:
            return (s[0] + "*" * 5 + s[at_sym - 1:]).lower()

        # Phone number
        S = "".join(i for i in s if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(S) - 10] + "***-***-" + S[-4:] 