class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def start_insert(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.start_insert(start.right, new_val)
            else:
                start.right = Node(new_val)

        else:
            if start.left:
                self.start_insert(start.left, new_val)
            else:
                start.left = Node(new_val)

    def insert(self, new_val):
        return self.start_insert(self.root, new_val)

    def start_search(self, start, find_val):
        if start != None:
            if start.value is find_val:
                return True
            elif start.value < find_val:
                return self.start_search(start.right, find_val)
            else:
                return self.start_search(start.left, find_val)

        return False

    def search(self, find_val):
        return self.start_search(self.root, find_val)

    def preorder_print(self, start, traversal=[]):
        if start:
            traversal.append(str(start.value))
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)        
        return traversal


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

print('-'.join(tree.preorder_print(tree.root)))