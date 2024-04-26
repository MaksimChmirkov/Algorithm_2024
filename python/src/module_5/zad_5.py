import math


def build_segment_tree(array, segment_tree, node, start, end):
    if start == end:
        segment_tree[node] = array[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(array, segment_tree, 2 * node + 1, start, mid)
        build_segment_tree(array, segment_tree, 2 * node + 2, mid + 1, end)
        segment_tree[node] = math.gcd(segment_tree[2 * node + 1],
                                      segment_tree[2 * node + 2])


def update_segment_tree(array, segment_tree, node, start, end, index, value):
    if start == end:
        array[index] = value
        segment_tree[node] = value
    else:
        mid = (start + end) // 2
        if start <= index <= mid:
            update_segment_tree(array, segment_tree, 2 * node + 1, start, mid,
                                index, value)
        else:
            update_segment_tree(array, segment_tree, 2 * node + 2, mid + 1,
                                end, index, value)
        segment_tree[node] = math.gcd(segment_tree[2 * node + 1],
                                      segment_tree[2 * node + 2])


def query_gcd(segment_tree, node, start, end, n, r):
    if r < start or end < n:
        return 0
    if n <= start and end <= r:
        return segment_tree[node]
    mid = (start + end) // 2
    left_gcd = query_gcd(segment_tree, 2 * node + 1, start, mid, n, r)
    right_gcd = query_gcd(segment_tree, 2 * node + 2, mid + 1, end, n, r)
    return math.gcd(left_gcd, right_gcd)


def main():
    N = int(input().strip())
    array = list(map(int, input().strip().split()))
    Q = int(input().strip())

    segment_tree_size = 2 * (2 ** (N - 1).bit_length()) - 1
    segment_tree = [0] * segment_tree_size

    build_segment_tree(array, segment_tree, 0, 0, N - 1)

    for _ in range(Q):
        query = input().strip().split()
        if query[0] == 's':
            n, r = int(query[1]) - 1, int(query[2]) - 1
            print(query_gcd(segment_tree, 0, 0, N - 1, n, r))
        elif query[0] == 'u':
            i, v = int(query[1]) - 1, int(query[2])
            update_segment_tree(array, segment_tree, 0, 0, N - 1, i, v)


if __name__ == "__main__":
    main()
