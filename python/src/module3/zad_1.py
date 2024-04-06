def rabin_karp(s, t):
    n = len(s)
    m = len(t)
    if n < m:
        return []

    hash_t = 0
    hash_s = 0
    base = 26
    prime = 101
    power = 1
    for i in range(m):
        hash_t = (hash_t * base + ord(t[i]) - ord('a')) % prime
        hash_s = (hash_s * base + ord(s[i]) - ord('a')) % prime
        if i > 0:
            power = (power * base) % prime

    indices = []
    for i in range(n - m + 1):
        if hash_s == hash_t:
            if s[i:i+m] == t:
                indices.append(i)
        if i < n - m:
            hash_s = (hash_s - power * (ord(s[i]) - ord('a'))) % prime
            hash_s = (hash_s * base + ord(s[i+m]) - ord('a')) % prime
            hash_s = (hash_s + prime) % prime

    return indices


s = input()
t = input()


result = rabin_karp(s, t)
for index in result:
    print(index, end=' ')
