class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
third.next = head

new = Node(40)

temp = head
while temp.next != head:
    temp = temp.next

temp.next = new
new.next = head

temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break
print("(back to head)")
