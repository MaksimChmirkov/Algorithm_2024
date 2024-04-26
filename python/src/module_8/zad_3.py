def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [start]
    visited = set()

    while queue:
        current_node = min(queue, key=lambda node: distances[node])
        queue.remove(current_node)
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    queue.append(neighbor)

    return distances


def main():
    N, M, K, C = map(int, input().split())
    capitals = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(M)]

    graph = {i: {} for i in range(1, N + 1)}
    for Ui, Vi, Ti in roads:
        graph[Ui][Vi] = Ti
        graph[Vi][Ui] = Ti

    distances = dijkstra(graph, C)

    results = [(capital, distances[capital]) for capital in capitals]
    results.sort(key=lambda x: x[1])

    for capital, time in results:
        print(capital, time)


if __name__ == "__main__":
    main()
