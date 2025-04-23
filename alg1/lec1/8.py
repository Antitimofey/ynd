a, b, n, m = [int(input()) for _ in range(4)]
d1 = (a*(n-1)+n, a*(n+1)+n)
d2 = (b*(m-1)+m, b*(m+1)+m)

d = (max(d1[0], d2[0]), min(d1[1], d2[1]))

#print(d1, d2, d)

if d[0] > d[1]:
    print(-1)
else:
    print(*d)