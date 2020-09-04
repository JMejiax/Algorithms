# AD-HOC - Problem #1

resultado = []
while True:
    try:
        a, b = map(str, input().split())
        # Convert an integer to a 32 bit representation
        a_32bit = "{:032b}".format(a)
        b_32bit = "{:032b}".format(b)

        c_sum_32bit = ""
        for i in range(0, len(a_32bit)):
            if a_32bit[i] == b_32bit[i]:
                c_sum_32bit = c_sum_32bit + "0"
            else:
                c_sum_32bit = c_sum_32bit + "1"
        # Convert a 32 bit to an integer representation
        c = int(c_sum_32bit, base=2)
        resultado.append(str(c))
    except Exception:
        break

print(*resultado, sep="\n")

