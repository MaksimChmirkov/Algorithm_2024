def can_reorder_train(N, train):
    stack = []
    current_wagon = 1

    for wagon in train:
        while stack and stack[-1] == current_wagon:
            stack.pop()
            current_wagon += 1

        if wagon == current_wagon:
            current_wagon += 1
        else:
            stack.append(wagon)

    while stack and stack[-1] == current_wagon:
        stack.pop()
        current_wagon += 1

    if not stack:
        return "YES"
    else:
        return "NO"


N = int(input())
train = list(map(int, input().split()))


result = can_reorder_train(N, train)
print(result)
