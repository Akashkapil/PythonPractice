# Space Complexity = O(1) as it uses a constant amount of space.
# Time Complexity = O(n), where n is the number of nodes in the linked list.

class Node:
    
    # constructor to initialize new node with data
    def __init__(self, data):
        self.data = data
        self.next = None

# function to Traverse the Linked list Iteratively
def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print() # for new line after printing all nodes

if __name__ == "__main__":
    node1 = Node(15)
    node2 = Node(45)
    node3 = Node(12)
    node4 = Node(10)

    head = node1

    node1.next = node2
    node2.next = node3
    node3.next = node4

    traverseList(head)