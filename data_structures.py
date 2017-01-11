'''
Trees:
- Have a node ('key'), may have additional info ('payload')
- Edge - connects two nodes to show there's a relationship
	- All nodes (minus root) connected by one incoming edge from another node
	- Nodes have have 1+ outgoing edges
- Root has no incoming edges; root of the tree
- Path is the ordered list of nodes connected by edges
- Children are set of nodes with incoming edges from same node
- Parent of all nodes it connects to w/outgoing edges
- Siblings share a Parent
- Subtree is a set of nodes, edges made of parent and all its descendants
- Leaf node is a node w/no children
- Level of a node n is number of edges on the path from the root node to n
- Height of tree is equal to the max level of any node in the tree

Binary tree - when each node in tree has max two children

'''

# Creating a tree using lists of lists
# [root, [left child / left subtree], [right child / right subtree]]

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print (tree.find(3)).v
print tree.find(10)
tree.deleteTree()
tree.printTree()