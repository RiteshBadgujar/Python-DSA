class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

top = None

value = int(input("Enter value to push: "))
new = Node(value)
new.next = top
top = new

value = int(input("Enter value to push: "))
new = Node(value)
new.next = top
top = new

if top is None:
    print("Stack is empty")
else:
    print("Popped:", top.data)
    top = top.next

temp = top
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
