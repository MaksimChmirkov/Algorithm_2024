class MaxElem:
    def __init__(sf, max_size):
        sf.heap = [0] * (max_size + 1)
        sf.size = 0

    def shift_up(sf, n):
        while n > 1 and sf.heap[n] > sf.heap[n // 2]:
            sf.heap[n // 2], sf.heap[n] = sf.heap[n], sf.heap[n // 2]
            n = n // 2
        return n

    def shift_down(sf, n):
        while 2 * n <= sf.size:
            left = 2 * n
            right = 2 * n + 1
            j = left
            if right <= sf.size and sf.heap[right] > sf.heap[left]:
                j = right
            if sf.heap[n] >= sf.heap[j]:
                break
            sf.heap[n], sf.heap[j] = sf.heap[j], sf.heap[n]
            n = j
        return n

    def insert(sf, value):
        if sf.size >= len(sf.heap) - 1:
            return -1
        sf.size += 1
        sf.heap[sf.size] = value
        return sf.shift_up(sf.size)

    def extract_max(sf):
        if sf.size == 0:
            return -1
        max_value = sf.heap[1]
        sf.heap[1] = sf.heap[sf.size]
        sf.size -= 1
        if sf.size > 0:
            new_index = sf.shift_down(1)
            return (new_index, max_value)
        return (0, max_value)


def print_elems(N, queries):
    pq = MaxElem(N)
    for query in queries:
        if query[0] == 1:
            if pq.size == 0:
                print(-1)
            else:
                result = pq.extract_max()
                print(result[0], result[1])
        elif query[0] == 2:
            result = pq.insert(query[1])
            print(result)

    print(' '.join(map(str, pq.heap[1:pq.size + 1])))


N, M = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(M)]
print_elems(N, queries)
