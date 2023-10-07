def Least_moves(x):
    step = 0
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x - 1
        step +=  1
    return step
# 例子
print(Least_moves(2))
print(Least_moves(5))
print(Least_moves(101))