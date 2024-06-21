class HashMap:
    def __init__(self, size = 30):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def _find_slot(self, key):
        hash_key = self._hash_function(key)
        index = hash_key
        while self.keys[index] and self.keys[index] != key:
            index = (index + 1) % self.size
            if index == hash_key:
                return None
        return index
    
    def set(self, key: str, value: int) -> None:
        index = self._find_slot(key)
        if index is None:
            return None
        self.keys[index] = key
        self.values[index] = value
        
    def get(self, key: str) -> int:
        index = self._find_slot(key)
        if index is None or self.keys[index] is None:
            return None
        return self.values[index]
    
    def delete(self, key: str) -> None:
        index = self._find_slot(key)
        if not index or not self.keys[index]:
            return
        self.keys[index] = None
        self.values[index] = None
    
    def printMap(self):
        for i in range(self.size):
            print(f"{i}: [{self.keys[i]}, {self.values[i]}]")
