a1, b1, a2, b2 = list(map(int, input().split()))

#a1 <-> a2
sq = (a1+a2)*(b1+b2)
res = ()
for v1 in (a1, b1):
    for v2 in (a2, b2):
        my_sq = max(v1, v2) * sum((a1+b1-v1, a2+b2-v2))
        if my_sq < sq:
            sq = my_sq
            res = (max(v1, v2), sum((a1+b1-v1, a2+b2-v2)))
print(res)