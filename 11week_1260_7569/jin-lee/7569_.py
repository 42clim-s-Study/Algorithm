"""
7569번 토마토
https://www.acmicpc.net/problem/7569
"""
from collections import deque
TM = 1
tm = 0


def bfs_3d(box, X, Y, Z, queue):
    while queue:
        z, y, x = queue.popleft()

        if z - 1 >= 0:
            if box[z - 1][y][x] == tm:
                box[z - 1][y][x] = box[z][y][x] + 1
                queue.append([z - 1, y, x])
        if z + 1 < Z:
            if box[z + 1][y][x] == tm:
                box[z + 1][y][x] = box[z][y][x] + 1
                queue.append([z + 1, y, x])

        if y - 1 >= 0:
            if box[z][y - 1][x] == tm:
                box[z][y - 1][x] = box[z][y][x] + 1
                queue.append([z, y - 1, x])
        if y + 1 < Y:
            if box[z][y + 1][x] == tm:
                box[z][y + 1][x] = box[z][y][x] + 1
                queue.append([z, y + 1, x])

        if x - 1 >= 0:
            if box[z][y][x - 1] == tm:
                box[z][y][x - 1] = box[z][y][x] + 1
                queue.append([z, y, x - 1])
        if x + 1 < X:
            if box[z][y][x + 1] == tm:
                box[z][y][x + 1] = box[z][y][x] + 1
                queue.append([z, y, x + 1])


def solution_001(tomato_box, X, Y, Z):
    days = 0
    is_exist_tm = False
    queue = deque()
    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if tomato_box[z][y][x] == TM:
                    queue.append([z, y, x])
                if tomato_box[z][y][x] == tm:
                    is_exist_tm = True

    if not is_exist_tm:
        return days

    bfs_3d(tomato_box, X, Y, Z, queue)

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if tomato_box[z][y][x] == tm:
                    days = -1
                    return days
                days = max(tomato_box[z][y][x], days)
    days = days - 1
    return days


if __name__ == "__main__":
    X, Y, Z = map(int, input().split())
    box = []
    for _ in range(Z):
        layer = []
        for _ in range(Y):
            layer.append(list(map(int, input().split())))
        box.append(layer)

    print(solution_001(box, X, Y, Z))
