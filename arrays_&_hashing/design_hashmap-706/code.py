class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> int:
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        bucket = self.buckets[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        bucket = self.buckets[hash_key]
        
        for k, v in bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        bucket = self.buckets[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

# Example usage:
myHashMap = MyHashMap()
myHashMap.put(1, 1)    # The map is now [[1,1]]
myHashMap.put(2, 2)    # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))  # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1)    # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))  # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2)    # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))  # return -1 (i.e., not found), The map is now [[1,1]]
