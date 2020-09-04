# Beginner - Problem #10

total = 0
for i in range(0, 2):
    code, units, amount = map(str, input().split())
    total = total + float(amount) * int(units)
print("VALOR A PAGAR: R$ " + "{:.2f}".format(total))

