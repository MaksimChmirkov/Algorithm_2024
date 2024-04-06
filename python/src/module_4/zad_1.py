def min_remove_to_make_valid(s):
    stack = []
    count = 0

    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                count += 1

    return count + len(stack)


s = input()
print(min_remove_to_make_valid(s))
