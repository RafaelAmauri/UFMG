class Node:
    def __init__(self, v):
        self.v = v
        self.right = None
        self.left = None

    def addChild(self, child):
        if child.v < self.v:
            self.left = child
        else:
            self.right = child


class Tree:
    def __init__(self, root):
        self.root = root
    
    def addNode(self, currentV, node):
        if node.v < currentV.v:
            if currentV.left is not None:
                self.addNode(currentV.left, node)
            else:
                currentV.addChild(node)
        else:
            if currentV.right is not None:
                self.addNode(currentV.right, node)
            else:
                currentV.addChild(node)

v0 = Node(0)
v1 = Node(1)
v2 = Node(2)
v3 = Node(3)
v4 = Node(4)
v5 = Node(5)
v6 = Node(6)

tree = Tree(v3)

tree.addNode(tree.root, v1)
tree.addNode(tree.root, v2)
tree.addNode(tree.root, v1)
tree.addNode(tree.root, v2)
tree.addNode(tree.root, v1)
tree.addNode(tree.root, v2)

print(tree.root.right.left)