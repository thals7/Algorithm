class hashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [None for _ in range(self.size+1)]

    def hashFunc(self, key):
        return key % 10

    def getAddress(self, key):
        hash_address = self.hashFunc(key)
        return hash_address

    def saveData(self, key, value):
        hash_address = self.hashFunc(key)
        while self.hash_table[hash_address] != None:
            if hash_address > self.size:
                hash_address = 0
            if self.hash_table[hash_address][0] == key: break
            hash_address += 1
        self.hash_table[hash_address] = (key, value)    
            
    def getData(self, key):
        hash_address = self.getAddress(key)
        while self.hash_table[hash_address] != None:
            if hash_address > self.size:
                hash_address = 0
            if self.hash_table[hash_address][0] == key: break
            hash_address += 1
        return self.hash_table[hash_address]

    def deleteData(self, key):
        hash_address = self.getAddress(key)
        while self.hash_table[hash_address] != None:
            if hash_address > self.size:
                hash_address = 0
            if self.hash_table[hash_address][0] == key:
                self.hash_table[hash_address] = None
                return True
            hash_address += 1
        else:
            return False

# practice
hash1 = hashTable(10)

hash1.saveData(1, 'A')
hash1.saveData(2, 'B')
hash1.saveData(10, 'C')

print(hash1.getData(1))
print(hash1.getData(2))
print(hash1.getData(10))

hash1.saveData(1,'D')
print(hash1.getData(1))

hash1.deleteData(1)
print(hash1.getData(1))
hash1.saveData(12, 'E')
print(hash1.getData(2))