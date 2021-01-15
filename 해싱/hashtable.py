class hashTable:
    def __init__(self, table_size):
        self.hash_table = [0 for i in range(table_size)]

    def hashFunc(self, key):
        return key % 10

    def getAddress(self, key):
        hash_address = self.hashFunc(key)
        return hash_address

    def saveData(self, key, value):
        hash_address = self.hashFunc(key)
        self.hash_table[hash_address] = value

    def getData(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]

    def deleteData(self, key):
        hash_address = self.getAddress(key)
        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False


# practice
hash1 = hashTable(10)

hashTable.saveData(hash1, 1, 'A')
hashTable.saveData(hash1, 2, 'B')
hashTable.saveData(hash1, 3, 'C')

print(hashTable.getData(hash1, 1))
print(hashTable.getData(hash1, 2))
print(hashTable.getData(hash1, 3))