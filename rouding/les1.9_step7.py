import math


l, w, h = map(int, input().split())
area1 = h * w
area2 = l * h
fin_area = (area1 + area2) * 2
print(math.ceil(fin_area / 16))
