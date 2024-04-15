# Insert a node at the tail end of a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
def insertNodeAtTail(head, data):
    if head is None: return SinglyLinkedListNode(data)

    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = SinglyLinkedListNode(data)

    return head
