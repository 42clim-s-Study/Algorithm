"""
1697번 숨바꼭질
https://www.acmicpc.net/problem/1697
"""
from collections import deque
INF = 999999
FIELD = 100001


def bfs(arr, start):
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if curr - 1 > 0:
            if arr[curr - 1] > arr[curr]:
                arr[curr - 1] = arr[curr] + 1
                queue.append(curr - 1)
        if curr + 1 < FIELD:
            if arr[curr + 1] > arr[curr]:
                arr[curr + 1] = arr[curr] + 1
                queue.append(curr + 1)
        if curr * 2 < FIELD:
            if arr[curr * 2] > arr[curr]:
                arr[curr * 2] = arr[curr] + 1
                queue.append(curr * 2)


if __name__ == "__main__":
    start, end = map(int, input().split())
    if start == end:
        print(0)
    elif start > end:
        print(start - end)
    else:
        arr = [INF for _ in range(0, FIELD)]
        arr[start] = 1
        bfs(arr, start)
        print(arr[end] - 1)
