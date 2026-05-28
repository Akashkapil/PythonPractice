# Node constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to add node at the begining
def insertAtBeginning(head, new_data):
    newNode = Node(new_data)
    newNode.next = head
    return newNode

# function to print the linked list
def printList(head):
    current = head
    while current is not None:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

# calling main function
if __name__ == "__main__":
    
    # initializing the nodes
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(40)

    # Linking the nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # initializing the head
    head = node1

    node_new = 12
    head = insertAtBeginning(head, node_new)

    printList(head)
