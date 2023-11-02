def Pascal_triangle(k):
    # 计算阶乘的辅助函数

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    
    # 计算组合数的辅助函数

    def combination(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    # 生成帕斯卡三角形的第 k 行

    return [combination(k-1, i) for i in range(k)]

print(Pascal_triangle(100))
print(Pascal_triangle(200))

