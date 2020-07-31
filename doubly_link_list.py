class DoubleLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoubleLinkedListNode(1)
b = DoubleLinkedListNode(2)
c = DoubleLinkedListNode(3)
a.next_node = b
b.next_node = c
b.prev_node = a
c.prev_node = b

print(a.value)
print(a.next_node.value)
print(a.prev_node.value)
print(b.next_node.value)
print(b.prev_node.value)
print(c.next_node.value)
print(a.prev_node.value)
