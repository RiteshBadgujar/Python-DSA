stack = []
n = int(input("How many elements to push: "))

for i in range(n):
    stack.append(int(input("Enter element: ")))

print("Stack:", stack)

# Pop one element
popped = stack.pop()
print("Popped element:", popped)
print("Stack after pop:", stack)
