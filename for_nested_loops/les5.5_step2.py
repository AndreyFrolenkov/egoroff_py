l = list(map(int, input().split()))
for i in l:
    for j in range(i):
        print('*', end='')
    print()
