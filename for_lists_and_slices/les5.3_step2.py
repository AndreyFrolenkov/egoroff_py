sub = input()
string = list(input().split())

for i in range(len(string)):
    if sub.upper() in string[i] or sub.lower() in string[i]:
        print(string[i])
