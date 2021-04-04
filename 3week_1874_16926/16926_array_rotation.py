# 16926
# 2 ≤ N, M ≤ 300
# 1 ≤ R ≤ 1,000
# min(N, M) mod 2 = 0
# 1 ≤ A_ij ≤ 108


def init_array(row: int, col: int):
    array = [[] for _ in range(row)]
    cdx = 0
    for i in range(1, row * col + 1):
        array[cdx].append(i)
        if i % col == 0:
            cdx += 1
    return array


# pypy3 : 메모리 125044 KB, 828 ms / python3 : 시간 초과)
def solution_001(row: int, col: int, rotation: int, matrix: list):
    layer = min(row, col) // 2
    # print(layer)
    # for elem in matrix:
    #     print(*elem)

    for _ in range(rotation):
        level = 0
        for lay in range(layer):
            i_r = lay
            i_c = lay
            if lay != 0:
                level += 1
            while i_c + 1 < col - level:
                matrix[i_r][i_c], matrix[i_r][i_c + 1] = matrix[i_r][i_c + 1], matrix[i_r][i_c]
                i_c += 1
            while i_r + 1 < row - level:
                matrix[i_r][i_c], matrix[i_r + 1][i_c] = matrix[i_r + 1][i_c], matrix[i_r][i_c]
                i_r += 1
            while i_c - 1 >= 0 + level:
                matrix[i_r][i_c], matrix[i_r][i_c - 1] = matrix[i_r][i_c - 1], matrix[i_r][i_c]
                i_c -= 1
            while i_r - 1 > 0 + level:
                matrix[i_r][i_c], matrix[i_r - 1][i_c] = matrix[i_r - 1][i_c], matrix[i_r][i_c]
                i_r -= 1
    for elem in matrix:
        print(*elem)


if __name__ == "__main__":
    row, col, rotation = map(int, input().split())
    # array = init_array(row, col)
    matrix = [list(map(int, input().split())) for _ in range(row)]
    solution_001(row, col, rotation, matrix)
