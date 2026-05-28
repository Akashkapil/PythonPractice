#  THIS IS A CLASSIC EXAMPLE OF SINGLY-LINKED-LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Node
node1 = Node(15)
node2 = Node(45)
node3 = Node(12)
node4 = Node(10)

# Linking the Nodes
node1.next = node2
node2.next = node3
node3.next = node4

# initilizing the Head (First node)
head = node1

# Traversing and printing the linked list
current = head
while current:
    print(current.data, end=" -> ") # this will help you in printing the whole values in a single line
    # print(f"{current.data}" + "-> ") # this will print each value in different line
    current = current.next
print("End")