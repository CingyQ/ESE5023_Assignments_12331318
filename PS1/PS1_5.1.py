def insert_operations(s, current='1'):
    if not s:  # 如果字符串为空，说明已经处理完所有数字
        return [current]

    # 分别代表插入+，-，或者什么都不插入
    plus_option = insert_operations(s[1:], current + '+' + s[0])

    minus_option = insert_operations(s[1:], current + '-' + s[0])

    join_option = insert_operations(s[1:], current + s[0])

    return plus_option + minus_option + join_option

def Find_expression(number):
    numbers = '23456789'
    all_combinations = insert_operations(numbers)
    for comb in all_combinations:
        if eval(comb) == number:
            print(comb + '=' + str(number))

# 示例：
Find_expression(50)