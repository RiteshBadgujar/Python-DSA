class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# COUNT nodes
count = 0
temp = head

while temp:
    count += 1
    temp = temp.next

print("Total nodes:", count)
