# 노드 생성
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# BST 구현
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 노드 삽입
    def insert(self, data):
        self.root = self.insertNode(self.root, data)
        return self.root

    def insertNode(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insertNode(node.left, data)
            else:
                node.right = self.insertNode(node.right, data)
        return node

    # 노드 탐색
    def find(self, data):
        return self.findNode(self.root, data)

    def findNode(self, node, data):
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self.findNode(node.left, data)
        elif data > node.data:
            return self.findNode(node.right, data)

    # 노드 삭제
    def delete(self, data):
        self.root, deleted = self.deleteData(self.root, data)
        return deleted

    def deleteData(self, node, data):
        if node is None:
            return node, False

        deleted = False
        # 해당 노드가 삭제할 노드인 경우
        if data == node.data:
            deleted = True
            # 삭제할 노드의 자식 노드가 2개인 경우
            if node.left and node.right:
                # 삭제할 노드의 Successor을 찾아 삭제할 노드의 위치와 교체
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                # 삭제할 노드의 왼쪽 자식 값을 successor 왼쪽 자식 노드로 붙임
                child.left = node.left
                if parent != node:  # Successor가 삭제할 노드의 오른쪽 자식이 아닌 경우
                    # successor의 부모 노드의 왼쪽 자식(원래 successor의 자리)을 successor의 오른쪽 자식으로 교체
                    parent.left = child.right
                    # successor의 오른쪽 자식을 삭제할 노드의 오른쪽 자식으로 교체
                    child.right = node.right
                node = child
            # 삭제할 노드의 자식 노드가 1개인 경우
            elif node.left or node.right:
                node = node.left or node.right
            # 삭제할 노드의 자식이 없는 경우
            else:
                node = None
        elif data < node.data:
            node.left, deleted = self.deleteData(node.left, data)
        else:
            node.right, deleted = self.deleteData(node.right, data)
        return node, deleted