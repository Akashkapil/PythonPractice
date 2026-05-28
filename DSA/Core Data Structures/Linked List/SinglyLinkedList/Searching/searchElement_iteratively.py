# Space complexity : O(1)
# Time Complexity : O(n) where n is number 

# Linked List node contructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# checks wether the element is present in the linked list
def searchElement(head, key):

    # initialize temp node to head of the linked list
    current = head

    # iterate over all the nodes
    while current:

        # if the node value is equal to the key then return the node
        if current.data == key:
            return True

        # if not then move to the next node
        current = current.next
    
    return False

# calling the main function
if __name__ == "__main__":
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # key to search in the Linked list
    key = 3

    if searchElement(head, key):
        print("True")
    else:
        print("False")