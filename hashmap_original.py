class HashMap:
    def __init__(self, size = 30):
        self.size = size
        self.map = [None for _ in range(float('inf'))] #Assume upper bound of hash() is float('inf')
        
    def _hash_function(self, key):
        return hash(key)
    
    def set(self, key: str, value: int) -> None:
        self.map[self._hash_function(key)] = value
    
    def get(self, key: str) -> int:
        hash_key = self._hash_function(key)
        if self.map[hash_key] is None:
            return -1
        return self.map[hash_key]
    
    def delete(self, key: str) -> None:
        hash_key = self._hash_function(key)
        self.map[hash_key] = None
    
    def printMap(self):
        for i in range(self.size):
            print(f"{i}: [{self.map[i]}]")