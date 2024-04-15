# binary search

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

# T=int(input())
T=int(6)
D = [2, 3, 7, 12, 16, 19, 20, 21, 30, 31, 32, 35, 36, 38, 90, 101, 123, 124, 240, 241, 390]
myTree=Solution()
root=None
for i in range(T):
    # data=int(input())
    data=D
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)