import heapq

graph = {
    1: [(2, 4), (3, 1)],
    2: [(4, 1)],
    3: [(2, 2), (4, 5)],
    4: []
}

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist

result = dijkstra(1)

for node in result:
    print(node, ":", result[node])
