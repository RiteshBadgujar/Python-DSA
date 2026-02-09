class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = int(input("Enter value to delete: "))

#first node
if head and head.data == key:
    head = head.next
else:
    prev = head
    curr = head.next

    while curr:
        if curr.data == key:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

#print list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
