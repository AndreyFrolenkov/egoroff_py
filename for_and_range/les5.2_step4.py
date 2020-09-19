n = int(input())
mishka = 0
cris = 0
for i in range(n):
    m, c = map(int, input().split())
    if m > c:
        mishka += 1
    elif c > m:
        cris += 1
if mishka > cris:
    print("Mishka")
elif cris > mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
