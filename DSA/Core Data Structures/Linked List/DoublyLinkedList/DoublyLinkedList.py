# Node Constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

if __name__ == "__main__":

    # Creating Node
    node1 = Node(15)
    node2 = Node(45)
    node3 = Node(12)
    node4 = Node(10)

    # Linking the node
    node1.prev = None
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3

    # setting up the head
    head = node1

    # traverse the list
    current = head
    while current is not None:
        print(current.data, end="")
        if current.next is not None:
            print("<->", end="")
        current = current.next



