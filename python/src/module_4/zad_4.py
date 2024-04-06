def st(s: list, n: int, k: int) -> list:
    res = []  # type: list[int]
    stack = []  # type: list[int]
    for i in range(n):
        while len(stack) != 0 and stack[0] <= i - k:
            stack.pop(0)
        while len(stack) != 0 and s[stack[-1]] >= s[i]:
            stack.pop()
        stack.append(i)
        if i >= k - 1:
            res.append(s[stack[0]])
    return res


n, k = map(int, input().split())
s = list(map(int, input().split()))

for i in st(s, n, k):
    print(i)
