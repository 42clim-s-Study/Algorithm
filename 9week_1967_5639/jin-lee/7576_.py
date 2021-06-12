"""
7576번 토마토
https://www.acmicpc.net/problem/7576

- dfs
모든 vertax 가 바둑판식으로 연결돼있는 순환 그래프이기 때문에,
직진성으로 순회하는 dfs 는 방문하지 않은 vertax 를 만날 때 까지 계속해서 순회한다.
가장 깊은 경로는 찾을 수 있겠지만, 최소 깊이로 모든 vertax 를 순회해야하는 7576번 문제에는 적합하지 않다.

- bfs
층(level)별로 순회하기 때문에, 최소 깊이로 모든 vertax 를 순회할 수 있다.
"""
from collections import deque
TM = 1
tm = 0


def bfs(tomato_box, width, height, queue):
    while queue:
        row, col = queue.popleft()
        if row - 1 >= 0:
            if tomato_box[row - 1][col] == tm:
                tomato_box[row - 1][col] = tomato_box[row][col] + 1
                queue.append([row - 1, col])
        if row + 1 < height:
            if tomato_box[row + 1][col] == tm:
                tomato_box[row + 1][col] = tomato_box[row][col] + 1
                queue.append([row + 1, col])
        if col - 1 >= 0:
            if tomato_box[row][col - 1] == tm:
                tomato_box[row][col - 1] = tomato_box[row][col] + 1
                queue.append([row, col - 1])
        if col + 1 < width:
            if tomato_box[row][col + 1] == tm:
                tomato_box[row][col + 1] = tomato_box[row][col] + 1
                queue.append([row, col + 1])


def solution_001(tomato_box, width, height):
    days = 0
    queue = deque()
    for r in range(height):
        for c in range(width):
            if tomato_box[r][c] == TM:
                queue.append([r, c])

    bfs(tomato_box, width, height, queue)

    for r in range(height):
        for c in range(width):
            if tomato_box[r][c] == tm:
                days = -1
                return days
            days = max(tomato_box[r][c], days)
    days = days - 1
    return days


if __name__ == "__main__":
    m, n = map(int, input().split())
    # box = [[0 for _ in range(m)] for _ in range(n)]
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    print(solution_001(box, m, n))
