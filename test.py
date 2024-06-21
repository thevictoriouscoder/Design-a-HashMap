import unittest
import hashmap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.map = hashmap.HashMap()
    
    def test_set_get(self):
        self.map.set("key1", 1)
        self.assertEqual(self.map.get("key1"), 1)
        self.map.set("key2", 2)
        self.assertEqual(self.map.get("key2"), 2)
        self.map.set("key1", 3)
        self.assertEqual(self.map.get("key1"), 3)
        
    def test_delete(self):
        self.map.set("key1", 1)
        self.map.delete("key1")
        self.assertIsNone(self.map.get("key1"))
        
    def test_delete_nonexistent(self):
        self.map.delete("key1") 
    
    def test_get_nonexistent(self):
        self.assertIsNone(self.map.get("randomKey"))
    
    def test_collision_handling(self):
        self.map.set("key1", 1)
        self.map.set("key11", 11)
        self.assertEqual(self.map.get("key1"), 1)
        self.assertEqual(self.map.get("key11"), 11)
        
    def test_large_input(self):
        for i in range(30):
            self.map.set(f"key{i}", i)
        for i in range(30):
            self.assertEqual(self.map.get(f"key{i}"), i)
    
    def test_print_map(self):
        for i in range(30):
            self.map.set(f"key{i}", i)
        self.map.printMap()
    
if __name__ == "__main__":
    unittest.main()
