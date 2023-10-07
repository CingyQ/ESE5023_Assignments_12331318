def insert_operations(s, current='1'):
    if not s:  # 如果字符串为空，说明已经处理完所有数字
        return [current]

    # 分别代表插入+，-，或者什么都不插入
    plus_option = insert_operations(s[1:], current + '+' + s[0])

    minus_option = insert_operations(s[1:], current + '-' + s[0])

    join_option = insert_operations(s[1:], current + s[0])

    return plus_option + minus_option + join_option



def Total_solutions(n):
    numbers = '23456789'
    all_combinations = insert_operations(numbers)
    count = 0
    for comb in all_combinations:
        if eval(comb) == n:
            count += 1
    return count

# 对1-100中的每个数字进行统计
result_counts = {i: Total_solutions(i) for i in range(1, 101)}
max_count = max(result_counts.values())
max_numbers = [k for k, v in result_counts.items() if v == max_count]
min_count = min(result_counts.values())
min_numbers = [k for k, v in result_counts.items() if v == min_count]
# 打印列表，检查结果
print(result_counts)
print(str(max_numbers)+" has the maximum number of Total_solutions is " + str(max_count))
print(str(min_numbers)+" has the minimum number of Total_solutions is " + str(min_count))

