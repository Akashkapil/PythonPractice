# time complexity = O(n)
# space complexity = O(1)

# Node constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):

    current = head
    prev = None

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    
    return prev

def printNode(head):
    
    while head:
        print(head.data, end="")
        if head.next != None:
            print("->", end="")
        head = head.next
    print()

# calling main function
if __name__ == "__main__":
    # creating linked list
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverse(head)
    printNode(head)  # output: 5->4->3->2->1
