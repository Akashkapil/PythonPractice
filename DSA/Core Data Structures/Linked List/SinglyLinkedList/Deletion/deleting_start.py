# Node constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# function to print the linked list
def printList(head):

    current = head

    while current:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

# function to delete the node at the begining
# # 1st method
# def delData(head):

    # if head is None:
    #     return head

#     temp_head = head

#     head = temp_head.next

#     temp_head.data = None

#     return head


# 2nd method
def delData(head):

    if head is None:
        return head

    temp_head = head

    head = head.next

    temp_head = None

    return head

# calling main function
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

    head = delData(head)

    printList(head)