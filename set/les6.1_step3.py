a = set(input().split())
b = set(input().split())
c = sorted(list(a - b))
for i in c:
    print(i, end=' ')
