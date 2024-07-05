class HashTable:
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]
    
    [[], [], [], [], []]

    def _hash(self, key):
        res = sum([ord(s) for s in key])
        return res % self.max_len