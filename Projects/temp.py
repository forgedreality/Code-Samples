# binary search
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    return 1 + max(lheight, rheight)


class BinaryTree:
    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return root
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

def solution(tree):
    out = BinaryTree()
    root = None
    for i in tree:
        root = out.insert(root, i)

    return height(root)

print(solution([1,2,3,4,-1,-1,-1]))