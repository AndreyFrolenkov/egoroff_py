# ticket = input()
# a = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# b = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
# if a == b:
#     print('YES')
# else:
#     print('NO')

tic = int(input())
a = tic // 100000 + tic // 10000 % 10 + tic // 1000 % 10
b = tic % 1000 // 100 + tic % 100 // 10 + tic % 10
if a == b:
    print("YES")
else:
    print("NO")
