def print_values(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        elif a > c:
            print(a, c, b)
        else:
            print(c, a, b)
    elif b > c:
        if a > c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        print(c, b, a)

# 例子
print_values(3, 1, 2)
print_values(10, 7, 21)
print_values(31, 12, 26)
print_values(99, 111, 222)
print_values(333, 1096, 2)