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
