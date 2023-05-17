class Node:
    def __init__(self,value):
        self.left = None
        self.Data = value
        self.right = None

class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,data,node):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(data,node.left)
        else:
            node.right = self.insert(data,node.right)
        return node
    