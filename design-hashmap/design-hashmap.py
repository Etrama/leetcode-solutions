class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.map.append([key, value])
        else:
            for index, val in enumerate(self.map):
                if val[0] == key:
                    self.map[index] = [key, value]
                    
    def get(self, key: int) -> int:
        for x, y in self.map:
            if x == key:
                return y
        return -1
        
    def remove(self, key: int) -> None:
        for index, value in enumerate(self.map):
            if value[0] == key:
                del self.map[index]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)