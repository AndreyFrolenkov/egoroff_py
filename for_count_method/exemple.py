# a = [1, 3, 4, 1, 0, 5, 5, 2, 3, 1, 1]
# s = [0] * 6
# for i in a:
#     s[i] += 1
# for j in range(len(s)):
#     print(str(j) * s[j])

import random


a = []
for i in range(10):
    a.append(random.randint(-10, 10))
count = [0] * 21
for i in a:
    count[i + 10] += 1
print(a)
for i in range(21):
    print(i - 10, count[i])

