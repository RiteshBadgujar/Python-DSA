from collections import deque

queue = deque()
n = int(input("How many elements to insert: "))

for i in range(n):
    queue.append(int(input("Enter element: ")))

print("Queue:", list(queue))

# Remove one element
removed = queue.popleft()
print("Removed element:", removed)
print("Queue after remove:", list(queue))
