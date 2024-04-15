'''
def sumTree(root):
    sums = []
    sums = calcSums(root, 0, sums)
    return sums


def calcSums(node, currentSum, sums):
    if not node:
        return 0

    newCurrSum = currentSum + node.value
    if not node.left and not node.right:
        sums.append(newCurrSum)

    calcSums(node.right, newCurrSum, sums)
    calcSums(node.left, newCurrSum, sums)

    return sums


class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right


def pushNode(root, val):
    new_node = Node(val)
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        node = queue.pop()

        if node.left is None:
            node.left = new_node
            break

        if node.right is None:
            node.right = new_node
            break

        queue.append(node.left)
        queue.append(node.right)


def buildTree(list):
    binaryTree = None
    for i in list:
        if i != -1:
            if binaryTree is not None:
                pushNode(binaryTree, i)
            else:
                binaryTree = Node(i)

    return binaryTree


def solution(arr):
    out = ""
    binaryTree = buildTree(arr)

    if binaryTree:
        if sumTree(binaryTree.left) > sumTree(binaryTree.right):
            return "Left"
        else:
            return "Right"

    return out
'''

# return the "Left" if left branch is larger
# "Right" if right is larger, "" if empty or equal branch sums
def solution(arr):
    if not arr:
        return ""
    left_sum = sum_tree(arr, 1)
    right_sum = sum_tree(arr, 2)

    return "Left" if left_sum > right_sum else "Right" if left_sum != right_sum else ""


def sum_tree(arr, node):
    if len(arr) <= node or arr[node] == -1:
        return 0
    return arr[node] + sum_tree(arr, 2 * node + 1) + sum_tree(arr, 2 * node + 2)

print(solution([3, 6, 2, 9, -1, 10]));