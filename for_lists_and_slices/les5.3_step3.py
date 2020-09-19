n = input().lower()
l = []
for i in range(len(n)):
    l.append(n.count(n[i]))
print(max(l))
