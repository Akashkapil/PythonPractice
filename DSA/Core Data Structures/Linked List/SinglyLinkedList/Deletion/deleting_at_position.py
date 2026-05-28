# constructor Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):

    current = head
    while current:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

def delPosition(head, position):

    temp_head = head
    
    if head is None:
        return head
    
    if position == 1:
        head = temp_head.next
        return head
    
    # traversing to the node before the one that needs to be deleted
    for i in range(1, position):
        prev = temp_head
        temp_head = temp_head.next

    # deleting the node at position
    prev.next = temp_head.next

    return head
