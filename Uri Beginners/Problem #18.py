values = [100, 50, 20, 10, 5, 2, 1]

number = int(input())

print(str(number))

for value in values:
    i = 0
    while value <= number:
        number = number - value
        i = i + 1
    print(str(i) + " nota(s) de R$ " + str(value) + ",00")

