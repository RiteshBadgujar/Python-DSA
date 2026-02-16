items = [
    (60, 10),   # (value, weight)
    (100, 20),
    (120, 30)
]

capacity = 50

items.sort(key=lambda x: x[0] / x[1], reverse=True)

total_value = 0

for value, weight in items:
    if capacity >= weight:
        total_value += value
        capacity -= weight
    else:
        fraction = capacity / weight
        total_value += value * fraction
        break

print("Maximum value:", total_value)
