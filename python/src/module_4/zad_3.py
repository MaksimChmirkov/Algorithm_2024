def find_nearest_smaller_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            result[idx] = i

        stack.append(i)

    return result


N = int(input())
arr = list(map(int, input().split()))


result = find_nearest_smaller_element(arr)


print(*result)
