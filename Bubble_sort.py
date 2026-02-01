n = int(input("Enter size: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

for i in range(n - 1):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted:", arr)
