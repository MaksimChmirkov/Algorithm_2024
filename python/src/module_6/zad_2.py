class MaxElem:
    def __init__(sf, max_size):
        sf.heap = [0] * (max_size + 1)
        sf.size = 0
        sf.index_map = {}

    def shift_up(sf, i):
        while i > 1 and sf.heap[i // 2] < sf.heap[i]:
            sf.index_map[sf.heap[i]], sf.index_map[sf.heap[i // 2]] = \
                sf.index_map[sf.heap[i // 2]], sf.index_map[sf.heap[i]]
            sf.heap[i // 2], sf.heap[i] = sf.heap[i], sf.heap[i // 2]
            i = i // 2
        return i

    def shift_down(sf, i):
        while 2 * i <= sf.size:
            left = 2 * i
            right = 2 * i + 1
            j = left
            if right <= sf.size and sf.heap[right] > sf.heap[left]:
                j = right
            if sf.heap[i] >= sf.heap[j]:
                break
            sf.index_map[sf.heap[i]], sf.index_map[sf.heap[j]] = \
                sf.index_map[sf.heap[j]], sf.index_map[sf.heap[i]]
            sf.heap[i], sf.heap[j] = sf.heap[j], sf.heap[i]
            i = j
        return i

    def insert(sf, value):
        if sf.size >= len(sf.heap) - 1:
            return -1
        sf.size += 1
        sf.heap[sf.size] = value
        sf.index_map[value] = sf.size
        return sf.shift_up(sf.size)

    def extract_max(sf):
        if sf.size == 0:
            return -1
        max_value = sf.heap[1]
        sf.heap[1] = sf.heap[sf.size]
        sf.index_map[sf.heap[1]] = 1
        sf.size -= 1
        if sf.size > 0:
            new_index = sf.shift_down(1)
            return (new_index, max_value)
        return (0, max_value)

    def remove_by_index(sf, index):
        if index < 1 or index > sf.size:
            return -1
        value = sf.heap[index]
        sf.heap[index] = sf.heap[sf.size]
        sf.index_map[sf.heap[index]] = index
        sf.size -= 1
        if sf.size > 0:
            sf.shift_down(index)
            sf.shift_up(index)
        return value


def process_queries(N, queries):
    pq = MaxElem(N)
    for query in queries:
        if query[0] == 1:
            result = pq.extract_max()
            if result == -1:
                print(-1)
            else:
                print(result[0], result[1])
        elif query[0] == 2:
            result = pq.insert(query[1])
            print(result)
        elif query[0] == 3:
            result = pq.remove_by_index(query[1])
            if result == -1:
                print(-1)
            else:
                print(result)

    print(' '.join(map(str, pq.heap[1:pq.size + 1])))


N, M = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(M)]

process_queries(N, queries)
