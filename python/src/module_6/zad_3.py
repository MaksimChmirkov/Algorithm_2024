class PyramidSort:
    def __init__(sf, heap):
        sf.heap = heap
        sf.size = len(heap)
        sf.build_heap()

    def parent(sf, i):
        return (i - 1) // 2

    def left_child(sf, i):
        return 2 * i + 1

    def right_child(sf, i):
        return 2 * i + 2

    def shift_up(sf, i):
        while i > 0 and sf.heap[i] > sf.heap[sf.parent(i)]:
            sf.heap[i], sf.heap[sf.parent(i)] = \
                  sf.heap[sf.parent(i)], sf.heap[i]
            i = sf.parent(i)

    def shift_down(sf, i):
        max_index = i
        left = sf.left_child(i)
        if left < sf.size and sf.heap[left] > sf.heap[max_index]:
            max_index = left
        right = sf.right_child(i)
        if right < sf.size and sf.heap[right] > sf.heap[max_index]:
            max_index = right
        if i != max_index:
            sf.heap[i], sf.heap[max_index] = \
                sf.heap[max_index], sf.heap[i]
            sf.shift_down(max_index)

    def build_heap(sf):
        for i in range(sf.size // 2, -1, -1):
            sf.shift_down(i)

    def pop(sf):
        max_value = sf.heap[0]
        sf.heap[0] = sf.heap[sf.size - 1]
        sf.size -= 1
        sf.heap.pop()
        sf.shift_down(0)
        return max_value


def heap_sort(heap):
    max_heap = PyramidSort(heap)
    sorted_array = []
    print(' '.join(map(str, max_heap.heap)))  # Вывод построенной кучи
    while max_heap.size > 0:
        max_value = max_heap.pop()
        sorted_array.append(max_value)
        if max_heap.size > 0:
            print(' '.join(map(str, max_heap.heap[:max_heap.size])))
    return sorted_array


n = int(input())
data = list(map(int, input().split()))
sorted_array = heap_sort(data)
sorted_array = sorted_array[::-1]
print(' '.join(map(str, sorted_array)))
