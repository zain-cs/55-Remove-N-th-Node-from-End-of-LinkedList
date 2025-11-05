class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        slow = dummy
        fast = dummy

        # Move fast ahead by n+1 steps
        for _ in range(n + 1):
            if fast:
                fast = fast.next

        # Move both until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node
        if slow.next:
            slow.next = slow.next.next

        # Update head
        self.head = dummy.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Create Linked List
ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.insert(val)

print("Original List:")
ll.print_list()

# Remove 2nd node from end
ll.remove_nth_from_end(2)

print("After Removing 2nd Node from End:")
ll.print_list()
