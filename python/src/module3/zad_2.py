def search(S, T):
    m = len(T)
    n = len(S)

    q = [0] * m
    j = 0

    find_q(T, m, q)

    i = 0
    while i < n:
        if T[j] == S[i]:
            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and T[j] != S[i]:
            if j != 0:
                j = q[j - 1]
            else:
                i += 1

    return -1


def find_q(T, m, q):
    len = 0
    q[0] = 0
    i = 1

    while i < m:
        if T[i] == T[len]:
            len += 1
            q[i] = len
            i += 1
        else:
            if len != 0:
                len = q[len - 1]
            else:
                q[i] = 0
                i += 1


S = input()
T = input()

res = search(T + T, S)
print(res)
