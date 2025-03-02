class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.exp_at = dict()        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.exp_at[tokenId] = currentTime + self.ttl        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.exp_at:
            return
        if currentTime < self.exp_at[tokenId]:
            self.exp_at[tokenId] = currentTime + self.ttl
        else:
            del self.exp_at[tokenId]        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for token in self.exp_at:
            if self.exp_at[token] > currentTime:
                res += 1
        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)