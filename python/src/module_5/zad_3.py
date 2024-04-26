def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def build_segment_tree(array, segment_tree, node, start, end):
    if start == end:
        segment_tree[node] = array[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(array, segment_tree, 2 * node + 1, start, mid)
        build_segment_tree(array, segment_tree, 2 * node + 2, mid + 1, end)
        segment_tree[node] = gcd(segment_tree[2 * node + 1],
                                 segment_tree[2 * node + 2])


def query_gcd(segment_tree, node, start, end, n, r):
    if r < start or end < n:
        return 0
    if n <= start and end <= r:
        return segment_tree[node]
    mid = (start + end) // 2
    left_gcd = query_gcd(segment_tree, 2 * node + 1, start, mid, n, r)
    right_gcd = query_gcd(segment_tree, 2 * node + 2, mid + 1, end, n, r)
    return gcd(left_gcd, right_gcd)


N = int(input().strip())
array = list(map(int, input().strip().split()))
K = int(input().strip())

segment_tree_size = 2 * (2 ** (N - 1).bit_length()) - 1
segment_tree = [0] * segment_tree_size

build_segment_tree(array, segment_tree, 0, 0, N - 1)

for _ in range(K):
    n, r = map(int, input().strip().split())
    print(query_gcd(segment_tree, 0, 0, N - 1, n - 1, r - 1))
