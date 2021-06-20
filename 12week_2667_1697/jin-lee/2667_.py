"""
2667번 단지번호붙이기
https://www.acmicpc.net/problem/2667
"""


def dfs(map, size, group, stack):
    buildings = 1
    while stack:
        row, col = stack.pop()
        if row - 1 >= 0:
            if map[row - 1][col] == 1:
                map[row - 1][col] = group
                buildings += 1
                stack.append([row - 1, col])
        if row + 1 < size:
            if map[row + 1][col] == 1:
                map[row + 1][col] = group
                buildings += 1
                stack.append([row + 1, col])
        if col - 1 >= 0:
            if map[row][col - 1] == 1:
                map[row][col - 1] = group
                buildings += 1
                stack.append([row, col - 1])
        if col + 1 < size:
            if map[row][col + 1] == 1:
                map[row][col + 1] = group
                buildings += 1
                stack.append([row, col + 1])
    return buildings


def solution_001(map, size):
    group = 2
    groups = []
    for i in range(size):
        for j in range(size):
            if map[i][j] == 1:
                stack = [[i, j]]
                temp = dfs(map, size, group, stack)
                if temp == 1:
                    groups.append(temp)
                else:
                    groups.append(temp - 1)
                group += 1
    print(group - 2)
    groups.sort()
    for buildings in groups:
        print(buildings)


if __name__ == "__main__":
    size = int(input())
    map = []
    for _ in range(size):
        buffer = int(input())
        row = [0 for _ in range(size)]
        for i in reversed(range(size)):
            row[i] += buffer % 10
            buffer = buffer // 10
        map.append(row)
    solution_001(map, size)
