n = int(input())
count = 0
while 2 ** count < n:
    count += 1
if 2 ** count == n:
    print(count)
else:
    print('НЕТ')
