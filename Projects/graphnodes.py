import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self, root):
        queue = [root]
        out = []
        while len(queue) > 0:
            current = queue.pop(0)  # removes first element, and returns it
            out.append(str(current.data))

            for neighbor in [current.left, current.right]:
                if neighbor is not None:
                    queue.append(neighbor)

        print(' '.join(out))


li = [3, 5, 4, 7, 2, 1]

myTree=Solution()
root=None

for i in range(6):
    data=int(li[i])
    root=myTree.insert(root,data)

print(myTree.levelOrder(root))
