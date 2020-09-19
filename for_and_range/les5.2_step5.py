n = int(input())
sub_string = "рок"
for i in range(n):
    string = input().lower()
    if string.find(sub_string) >= 0:
        print(i + 1, string.find(sub_string) + 1)
# s = input().lower()
# print(s)
# print(s.find(sub_sring) + 1)