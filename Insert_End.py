class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_end(head, value):
    new = Node(value)

    if head is None:
        return new

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new
    return head

# example
head = None
head = insert_end(head, 10)
head = insert_end(head, 20)
head = insert_end(head, 30)

temp = head
while temp:
    print(temp.data)
    temp = temp.next
