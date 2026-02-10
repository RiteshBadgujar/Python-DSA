class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = int(input("Enter value to search: "))

found = False
temp = head
pos = 1

while temp:
    if temp.data == key:
        print("Found at position:", pos)
        found = True
        break
    temp = temp.next
    pos += 1

if not found:
    print("Not Found")
