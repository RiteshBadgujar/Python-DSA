n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

start = 0
end = n - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed array:", arr)
