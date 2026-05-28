# Node class constructor
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

# function to insert a node in a specific postition
def insertNode(head, position, data):

    # checking the edge cases here
    if position < 1:
        return head

    # head will change if position is 1
    if position == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    # initializing a new temp head variable
    new_head = head

    # Traverse to the node which is just before the new node
    for i in range(1, position - 1):
        if new_head is None:
            return head
        new_head = new_head.next

    # if position is greater than number of nodes
    if new_head is None:
        return head

    # creating new node
    new_node = Node(data)

    # updating the next pointers
    new_node.next = new_head.next
    new_head.next = new_node

    return head
    
# calling the main function
if __name__ == "__main__":

    # creating the nodes
    node1 = Node(10)
    node2 = Node(30)
    node3 = Node(50)
    node4 = Node(15)
    node5 = Node(60)
    node6 = Node(80)

    # Linking the nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    # setting up the head
    head = node1

    val, pos = 95, 3
    head = insertNode(head, pos, val)

    printList(head)
