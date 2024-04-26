def tree(N, e):
    if len(e) != N - 1:
        return "NO"

    adj_list = {i: [] for i in range(1, N + 1)}
    for u, v in e:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [False] * (N + 1)
    stack = [1]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(adj_list[node])

    if not all(visited[1:]):
        return "NO"

    cycle_found = [False]
    visited = [False] * (N + 1)
    dfs(1, -1, adj_list, visited, cycle_found)

    if cycle_found[0]:
        return "NO"

    return "YES"


def dfs(node, parent, adj_list, visited, cycle_found):
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor, node, adj_list, visited, cycle_found)
        elif neighbor != parent:
            cycle_found[0] = True
            return


N, M = map(int, input().split())
e = [tuple(map(int, input().split())) for _ in range(M)]

print(tree(N, e))
