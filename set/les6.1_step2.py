a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = set(a)
b1 = set(b)
d = a1.intersection(b1)
for i in d:
    print(i, end=' ')
