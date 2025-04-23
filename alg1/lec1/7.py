n, k, m = list(map(int, input().split()))


def melt(n, k, m):
    semis = n//k
    details = semis*(k//m)
    rest = n%k + semis*(k%m)
    if rest < k:
        return details
    return details + melt(rest, k, m)

if k < m:
    print(0)
else:
    print(melt(n, k, m))