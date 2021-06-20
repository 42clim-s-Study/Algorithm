"""
2206번 벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
"""
from collections import deque
from copy import deepcopy
MAX = 1000000


def break_wall(map, breaked, row, col):
    if [row, col] not in breaked and breaked[0] == 1:
        map[row][col] = 0
        breaked.append([row, col])
        breaked[0] = 0


def bfs(clone, breaked, height, width):
    queue = deque()
    queue.append([0, 0])
    clone[0][0] = 1
    while queue:
        row, col = queue.popleft()

        if row - 1 >= 0:
            if clone[row - 1][col] == 1:
                break_wall(clone, breaked, row - 1, col)
            if clone[row - 1][col] == 0:
                clone[row - 1][col] = clone[row][col] + 1
                queue.append([row - 1, col])

        if row + 1 < height:
            if clone[row + 1][col] == 1:
                break_wall(clone, breaked, row + 1, col)
            if clone[row + 1][col] == 0:
                clone[row + 1][col] = clone[row][col] + 1
                queue.append([row + 1, col])

        if col - 1 >= 0:
            if clone[row][col - 1] == 1:
                break_wall(clone, breaked, row, col - 1)
            if clone[row][col - 1] == 0:
                clone[row][col - 1] = clone[row][col] + 1
                queue.append([row, col - 1])

        if col + 1 < width:
            if clone[row][col + 1] == 1:
                break_wall(clone, breaked, row, col + 1)
            if clone[row][col + 1] == 0:
                clone[row][col + 1] = clone[row][col] + 1
                queue.append([row, col + 1])

    return clone[height - 1][width - 1]


if __name__ == "__main__":
    row, col = map(int, input().split())
    map = []
    wall = 0
    for _ in range(row):
        buffer = int(input())
        line = [0 for _ in range(col)]
        for i in reversed(range(col)):
            is_wall = buffer % 10
            if is_wall:
                wall += 1
            line[i] += is_wall
            buffer = buffer // 10
        map.append(line)
    breaked = [0]
    best_case = MAX
    for _ in range(wall):
        clone = deepcopy(map)
        breaked[0] = 1
        now = bfs(clone, breaked, row, col)
        if now and now < best_case:
            best_case = now
    if best_case == MAX:
        print(-1)
    else:
        print(best_case)
