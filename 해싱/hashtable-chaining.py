# Chaining(연결리스트)를 이용한 해쉬 테이블 충돌 방지
# 참고: https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python

class listNode:
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None


class hashTable:
    def __init__(self, table_size):
        self.hash_table = [listNode(-1) for _ in range(table_size)]

    def hashFunc(self, key):
        return key % 10

    def getAddress(self, key):
        hash_address = self.hashFunc(key)
        return hash_address

    def saveData(self, key, value): # dummy node 이용
        hash_address = self.hashFunc(key)
        head = self.hash_table[hash_address]
        cur = head.next
        while cur:
            if cur.key == key: break# 동일한 키값이 존재할 경우 while문 탈출하여 value값만 업데이트
            cur = cur.next
        else: # 해당주소값에 데이터가 비어있거나 연결리스트를 순회하며 동일한 key값을 찾지 못한 경우
            cur = listNode(key)
            cur.next = head.next # 새 노드는 연결리스트의 head 바로 뒤에 추가
            head.next = cur
        cur.val = value

    def getData(self, key):
        hash_address = self.getAddress(key)
        cur = self.hash_table[hash_address].next
        while cur:
            if cur.key == key: break
            cur = cur.next
        else:
            return -1
        return cur.val

    def deleteData(self, key):
        hash_address = self.getAddress(key)
        cur = self.hash_table[hash_address]
        while cur and cur.next: # 삭제시에는 삭제할 노드의 직전 노드 또한 알고 있어야 함
            if cur.next.key == key: break # 삭제할 키를 찾은 경우
            cur = cur.next
        else:
            return None
        cur.next = cur.next.next


# practice
hash1 = hashTable(10)

hash1.saveData(1, 'A')
hash1.saveData(2, 'B')
hash1.saveData(3, 'C')

print(hash1.getData(1))
print(hash1.getData(2))
print(hash1.getData(3))

hash1.saveData(1,'D')
print(hash1.getData(1))

hash1.saveData(11, 'E')
print(hash1.getData(11))
hash1.deleteData(1)
print(hash1.getData(1))