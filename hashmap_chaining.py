class HashMap:
    def __init__(self, size = 30):
        self.size = size
        self.map = [[] for _ in range(30)]
        
    def _hash_function(self, key):
        return hash(key) % len(self.map)
    
    def set(self, key: str, value: int) -> None:
        hash_key = self._hash_function(key)
        for pair in self.map[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[hash_key].append([key, value])
    
    def get(self, key: str) -> int:
        hash_key = self._hash_function(key)
        for pair in self.map[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key: str) -> None:
        hash_key = self._hash_function(key)
        items = self.map[hash_key]
        for i in range(len(items)):
            if items[i][0] == key:
                del items[i]
                return
    
    def printMap(self):
        for i in range(self.size):
            print(f"{i}: [{self.map[i]}]")