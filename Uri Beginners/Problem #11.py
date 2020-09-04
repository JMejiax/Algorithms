# Beginner - Problem #11
# print("VOLUME = " + "{:.3f}".format((4.0/3) * 3.14159 * (float(input())**3)))

# Beginner - Problem #12

num1, num2, num3 = map(str, input().split())
print("TRIANGULO: " + "{:.3f}".format((float(num1)*float(num3))/2)
      + "\nCIRCULO: " + "{:.3f}".format((float(num3)**2 * 3.14159))
      + "\nTRAPEZIO: " + "{:.3f}".format(((float(num1)+float(num2))/2.0) * float(num3))
      + "\nQUADRADO: " + "{:.3f}".format((float(num2)**2))
      + "\nRETANGULO: " + "{:.3f}".format((float(num1)*float(num2))))


