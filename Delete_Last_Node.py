class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

if head is None:
    pass
elif head.next is None:
    head = None
else:
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
