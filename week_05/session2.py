class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # For testing
    @staticmethod
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next


# Problem 2
shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
link = Node("Link")
toad = Node("Toad")

shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

# Print current list
print("Current List:")
Node.print_linked_list(shy_guy)

# Updated list
shy_guy.next = link
link.next = diddy_kong
diddy_kong.next = toad
toad.next = dry_bones

print("Updated List:")
Node.print_linked_list(shy_guy)


# Problem 3
def add_second(head, val):
    # Create a new node
    new_node = Node(val)

    new_node.next = head.next

    head.next = new_node

    return head


original_list_head = Node("banana")
second = Node("blue shell")
third = Node("bullet bill")
original_list_head.next = second
second.next = third

# Linked list before insertion: "banana" -> "blue shell" -> "bullet bill"
print("Original List:")
Node.print_linked_list(original_list_head)

new_list = add_second(original_list_head, "red shell")

print("List After Insertion:")
Node.print_linked_list(new_list)

# Problem 4
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def increment_ll(head):
    current = head
    while current:
        current.value += 1
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

#example usage
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(increment_ll(node_one))


# problem 5
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def copy_ll(head):
    pass



mario = Node("Mario")
daisy = Node("Daisy")
luigi = Node("Luigi")
mario.next = daisy
daisy.next = luigi

# Linked List: Mario -> Daisy -> Luigi
copy = copy_ll(mario)

# Change original list -- should not affect the copy
mario.value = "Original Mario"

print_linked_list(head)
print_linked_list(copy) 