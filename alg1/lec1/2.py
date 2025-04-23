lst = [int(input()) for _ in range(3)]


lst = sorted(lst)

print(lst)

if lst[1] + lst[0] > lst[2]:
    print( 'YES')
else:
    print('NO')
