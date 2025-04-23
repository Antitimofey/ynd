a, b, c = [int(input()) for _ in range (3)]

def foo(a, b, c):
    if c < 0:
        print('NO SOLUTION')
        return

    if a == 0:
        if b == c**2:
            print('MANY SOLUTIONS')
            return
        else:
            print('NO SOLUTION')
            return
    res = (c**2-b)/a
    if res % 1 != 0:
        print('NO SOLUTION')
        return
    print(int((c**2-b)/a))

foo(a, b, c)


# ax+b=c**2
# ax=c**2-b
# x=(c**2-b)/a if a != 0 else a == 0 => ax == 0 => b?=c**2