class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.prev = head
second.next = third
third.prev = second

new = Node(40)

temp = head
while temp.next:
    temp = temp.next

temp.next = new
new.prev = temp

temp = head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")
