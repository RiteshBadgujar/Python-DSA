class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# nodes created
head = Node(10)
second = Node(20)
third = Node(30)

# link
head.next = second
second.next = third

# traverse
temp = head
while temp:
    print(temp.data)
    temp = temp.next
