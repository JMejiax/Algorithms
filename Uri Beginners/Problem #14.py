
# Beginner - Problem #14
import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
p1 = (x2 - x1)**2
p2 = (y2 - y1)**2

resul = math.sqrt(p1 + p2)

print("{:.4f}".format(resul)) 

