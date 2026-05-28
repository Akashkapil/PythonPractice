# The time complexity is O(n), where n is the number of nodes in the linked list. This is because the function makes a single recursive call for each node, and each call performs a constant amount of work (printing data and checking the next node).
# The space complexity is O(n), due to the recursion stack. Each recursive call adds a frame to the call stack, and the maximum depth is equal to the number of nodes. This is not optimized for very large lists, as it could lead to stack overflow errors in some environments.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# function to Traverse the Linked list Recursively
def traverseList(head):
    
    # Base condition when the head is None
    if head is None:
        print()
        return
    
    # printing the current node data
    print(head.data, end="")

    # printing arrow if its not the last node
    if head.next is not None:
        print(" -> ", end="")

    # moving to the next node
    traverseList(head.next)

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