class RandomizedSet:

    def __init__(self):
        self.dataset = {}

    def insert(self, val: int) -> bool:
        if not self.dataset.get(val,False):
            self.dataset[val]=1
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.dataset.pop(val,False):
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.dataset.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()