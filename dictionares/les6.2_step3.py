n = int(input())
sl = {}
# d = {i: i ** 2 for i in range(1, n + 1)}
# print(d)
for num in range(1, n + 1):
    sl[num] = num ** 2
print(sl)