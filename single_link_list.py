# Singly Link List
'''
1. A singly linked list is a collection of nodes that collectively form a linear sequences
2. Each node stores a reference to an object that is element of the sequence, as well as a reference to next node of the list 
3. Head in the list identifies the first node of the list 
4. tail identifies the last node of the list 
5. Traversing is done in each node of the linked list i.e. Traversing means visiting each node of the list once in order to perform some operation on that
6. Cycle check is the problem where we check the circular link list i.e. reference of the last link list identifies the first node of the list  
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    # Link List Reversal


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b

b.next_node = c

print(a.value)

print(a.next_node.value)

print(b.next_node.value)

# AttributeError: 'NoneType' object has no attribute 'value'
print(c.next_node.value)

# Singly Link List Cycle Check Circular Link List
c.next_node = a
print(c.next_node.value)

# Reverse List -


def reverse(head):
    current = head
    prev = None
    next_node = None
    while current:
        next_node = current.next_node
        current.next_node = prev
        prev = current
        current = next_node
    return prev


reverse(a)
print(d.next_node.value)
