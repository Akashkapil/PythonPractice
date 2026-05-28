# Space Complexity : O(n)
# Time Complextiy : O(n)

# Node class constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Recursive function to search an element
def searchElement(head, key):

    if head is None:
        return False

    # checking if the key is the first element
    if head.data == key:
        return True
    
    return searchElement(head.next, key)

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