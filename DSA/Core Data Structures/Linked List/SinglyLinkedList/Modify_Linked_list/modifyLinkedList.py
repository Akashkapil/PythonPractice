# using array approach space - O(n) time - O(n)
# we will use the approach given below

# Node constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# function to reverse the linked list iteratively
def reverseList(head):

    # initialize previous, next and current pointers
    prev = None
    current = head

    # Traverse and reverse the linked list
    while current is not None:
        next_node = current.next

        # reversing the current node's pointer
        current.next = prev
        
        # Reverse the current node's pointer
        current.next = prev
        prev = current
        current = next_node

    return prev

# Function to modify the linked list
def modifyTheList(head):
  
    # Returning head if list has only one node
    if head.next is None:
        return head

    slow = head
    fast = head

    # Finding the middle node of the linked list
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    mid = slow

    # Storing the second half of the list starting
    # after the middle node
    reversed_list = mid.next

    # Splitting the list into two halves
    mid.next = None

    # Reversing the second half of the list
    reversed_list = reverseList(reversed_list)

    curr1 = head
    curr2 = reversed_list

    # Iterating over both halves of the list 
    # and modifying the values
    while curr2 is not None:
        x = curr1.data
        curr1.data = curr2.data - x
        curr2.data = x
        curr1 = curr1.next
        curr2 = curr2.next

    # Reversing the second half of the list 
    # again and connecting both halves
    mid.next = reverseList(reversed_list)
    
    return head

def print_list(node):
    curr = node
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == "__main__":
  
    # Create a hard-coded linked list
    # 10 -> 4 -> 5 -> 3 -> 6
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    print_list(head)

