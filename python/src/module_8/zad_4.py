def dijkstra_algo(graph, start, num_nodes):
    dists = [float('inf')] * (num_nodes + 1)
    dists[start] = 0
    visited = [False] * (num_nodes + 1)

    for _ in range(num_nodes):
        min_distance = float('inf')
        min_node = None
        for node in range(1, num_nodes + 1):
            if not visited[node] and dists[node] < min_distance:
                min_distance = dists[node]
                min_node = node

        if min_node is None:
            break

        visited[min_node] = True
        for nearpos, weight in graph[min_node]:
            dist = dists[min_node] + weight
            if dist < dists[nearpos]:
                dists[nearpos] = dist

    return dists


def find_pos(N, roads):
    graph = {i: [] for i in range(1, N + 1)}
    for road in roads:
        u, v, w = road
        graph[u].append((v, w))
        graph[v].append((u, w))

    max_distances = []
    for i in range(1, N + 1):
        distances = dijkstra_algo(graph, i, N)
        max_distance = max(distances[1:])
        max_distances.append((max_distance, i))

    max_distances.sort()
    return max_distances[0][1]


N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

pos = find_pos(N, roads)
print(pos)
