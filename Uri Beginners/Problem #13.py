# Beginner - Problem #13

a, b, c = map(int, input().split())
ab = int((a + b + abs(a-b))/2)
ac = int((a + c + abs(a-c))/2)
if ab > ac:
    print(str(ab) + " eh o maior")
else:
    print(str(ac) + " eh o maior")


