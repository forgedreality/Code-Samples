# Insert a node at the tail end of a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
def insertNodeAtHead(llist, data):
    if llist is None: llist = SinglyLinkedListNode(data)
    else:
        head = SinglyLinkedListNode(data)
        head.next = llist
        llist = head

    return llist
