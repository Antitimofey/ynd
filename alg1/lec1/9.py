br = [int(input()) for _ in range(3)]
wall = [int(input()) for _ in range(2)]

br = sorted(br)

if br[0] <= min(wall) and br[1] <= max(wall):
    print('YES')
else:
    print('NO')