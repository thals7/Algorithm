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

hash1.saveData(1, 'A')
hash1.saveData(2, 'B')
hash1.saveData(3, 'C')

print(hash1.getData(1))
print(hash1.getData(2))
print(hash1.getData(3))

hash1.deleteData(1)
print(hash1.getData(1))
hash1.saveData(11, 'D')
print(hash1.getData(1)) # 실행시 D가 print됨 (1과 11의 해쉬주소가 같기 때문) -> 충돌 방지 필요