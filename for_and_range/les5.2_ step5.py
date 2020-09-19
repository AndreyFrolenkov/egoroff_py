n = int(input())
l = []
for i in range(n):
    string = input()
    if not "соль" in string:
        l.append(string)
print(", ".join(l))
