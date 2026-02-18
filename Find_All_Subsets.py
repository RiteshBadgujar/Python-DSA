def subsets(arr, index, current):
    if index == len(arr):
        print(current)
        return

    subsets(arr, index + 1, current)
    subsets(arr, index + 1, current + [arr[index]])

arr = [1, 2, 3]
subsets(arr, 0, [])
