class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = None
rear = None

value = int(input("Enter value to enqueue: "))
new = Node(value)

if rear is None:
    front = rear = new
else:
    rear.next = new
    rear = new

value = int(input("Enter value to enqueue: "))
new = Node(value)

if rear is None:
    front = rear = new
else:
    rear.next = new
    rear = new

if front is None:
    print("Queue is empty")
else:
    print("Dequeued:", front.data)
    front = front.next
    if front is None:
        rear = None

temp = front
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
