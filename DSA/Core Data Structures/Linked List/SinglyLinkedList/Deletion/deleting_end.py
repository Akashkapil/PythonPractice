# Node constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# printing the linked list
def printList(head):

    current = head

    while current:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

# function for delete the last node
def delLast(head):

    if head is None:
        return head
    
    temp_head = head

    while temp_head.next.next is not None:
        temp_head = temp_head.next

    temp_head.next = None

    return head

# calling main function
if __name__ == "__main__":

    # creating nodes
    node1 = Node(20)
    node2 = Node(40)
    node3 = Node(14)
    node4 = Node(70)

    # Linking the nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = node1

    head = delLast(head)

    printList(head)
