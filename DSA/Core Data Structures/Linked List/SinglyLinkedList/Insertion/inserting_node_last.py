# Node initilaizing constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print the Linked List
def printList(head):
    current = head
    while current is not None:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

# function to add node to the end of the Linked list
def insertAtEnd(head, new_data):
    
    # create a new node with given data
    new_node = Node(new_data)

    # if the Linked list is empty the return the node
    if head is None:
        return new_node
    
    # storing the head in a temp variable
    temp_head = head

    # traversing till the last node
    while temp_head.next is not None:
        temp_head = temp_head.next

    # changing the pointer of the last node to the new node
    temp_head.next = new_node

    return head

# creating the main function

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

    new_node_data = 90

    head = node1

    head = insertAtEnd(head, new_node_data)

    printList(head)
