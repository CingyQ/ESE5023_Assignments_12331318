import random

M1 = [[random.randint(0, 50) for _ in range(10)] for _ in range(5)]
M2 = [[random.randint(0, 50) for _ in range(5)] for _ in range(10)]
print("M1:")
for row in M1:
    print(row)
print("M2:")
for row in M2:
    print(row)


def Matrix_multip(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    # print("result:")
    # for row in result:
    #     print(row)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Multiply M1 and M2
result_matrix = Matrix_multip(M1, M2)
print("result_matrix:")
for row in result_matrix:
    print(row)
