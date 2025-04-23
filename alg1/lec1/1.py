start, end = input().split()
start = int(start)
end = int(end)
mode = input()

#print(start, end, mode)


def des(start, end, mode):
    def res(mode: str):
        if mode == 'heat':
            if end < start:
                return start
            return end
        elif mode == 'freeze':
            if end > start:
                return start
            return end
        raise Exception('bad argument  mode')
        
    if mode == 'auto':
        if end > start:
            print(res('heat'))
        else:
            print(res('freeze'))
    elif mode == 'fan':
        print(start)
    else:
        print(res(mode))


des(start, end, mode)
'''
for e in range(-20, 21, 10):
    for m in ['heat', 'freeze', 'auto', 'fan']:
        print(0, e, m, 'rees is', end='\t')
        des(0, e, m)
'''