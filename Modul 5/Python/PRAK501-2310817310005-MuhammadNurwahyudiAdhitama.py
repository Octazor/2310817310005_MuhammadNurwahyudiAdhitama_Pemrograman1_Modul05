def max_bilangan(num1, num2, num3, num4):
    max_val = num1

    if num2 > max_val:
        max_val = num2
    if num3 > max_val:
        max_val = num3
    if num4 > max_val:
        max_val = num4

    return max_val

a, b, c, d = map(int, input("").split())
hasil = max_bilangan(a, b, c, d)
print(hasil)
