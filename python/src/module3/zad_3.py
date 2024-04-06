def compute_z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def find_max_concatenated_string(s):
    z = compute_z_function(s)
    n = len(s)
    max_k = 1
    for i in range(1, n):
        if i + z[i] == n and n % i == 0:
            max_k = max(max_k, n // i)
    return max_k


s = input().strip()


result = find_max_concatenated_string(s)
print(result)
