# Singly Linked List
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/submissions/
def printLinkedList(head):
    l = head
    while l is not None:
        print(l.data)
        l = l.next
