def preprocess(arr):
    prefix_zeros = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_zeros[i] = prefix_zeros[i - 1] + (arr[i - 1] == 0)
    return prefix_zeros


def find_kth_zero_optimized(prefix_zeros, n, r, k):
    zeros_count = prefix_zeros[r] - prefix_zeros[n - 1]
    if zeros_count < k:
        return -1
    left, right = n, r
    while left < right:
        mid = (left + right) // 2
        if prefix_zeros[mid] - prefix_zeros[n - 1] >= k:
            right = mid
        else:
            left = mid + 1
    return left


N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

prefix_zeros = preprocess(arr)

results = []
for _ in range(Q):
    n, r, k = map(int, input().split())
    result = find_kth_zero_optimized(prefix_zeros, n, r, k)
    results.append(result)

print(*results)
