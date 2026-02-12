class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

pos = int(input("Enter position: "))
value = int(input("Enter value: "))

new = Node(value)

if pos == 1:
    new.next = head
    head = new
else:
    temp = head
    count = 1

    while temp and count < pos - 1:
        temp = temp.next
        count += 1

    if temp:
        new.next = temp.next
        temp.next = new

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
