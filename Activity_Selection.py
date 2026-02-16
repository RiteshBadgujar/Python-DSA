activities = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]

activities.sort(key=lambda x: x[1])

selected = []
last_end = 0

for start, end in activities:
    if start >= last_end:
        selected.append((start, end))
        last_end = end

print("Selected activities:")
for act in selected:
    print(act)
