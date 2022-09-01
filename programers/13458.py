class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
add(3)
add(4)
add(5)

node = head
while node.next:
    print(node.data)
    node=node.next
print(node.data)
print(head)



print(node1.next.data)
# print(node2.data)