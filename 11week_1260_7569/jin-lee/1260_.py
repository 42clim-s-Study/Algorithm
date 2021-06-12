"""
1260번 DFS와 BFS
https://www.acmicpc.net/problem/1260
"""

from collections import deque
from copy import deepcopy


def dfs(start, list, count):
    stack = [start]
    seq = []
    visited = [0 for _ in range(count + 1)]
    while stack:
        curr = stack.pop()
        if visited[curr] == 0:
            seq.append(curr)
        visited[curr] = 1
        while list[curr]:
            tmp = list[curr].pop()
            if not visited[tmp]:
                stack.append(tmp)
    return seq


def bfs(start, list, count):
    queue = deque([start])
    seq = []
    visited = [0 for _ in range(count + 1)]
    while queue:
        curr = queue.popleft()
        if visited[curr] == 0:
            seq.append(curr)
        visited[curr] = 1
        while list[curr]:
            tmp = list[curr].pop()
            if not visited[tmp]:
                queue.append(tmp)
    return seq


if __name__ == "__main__":
    count, connection, start = map(int, input().split())
    adj_list = [[] for _ in range(count + 1)]
    for _ in range(connection):
        vertax_1, vertax_2 = map(int, input().split())
        adj_list[vertax_1].append(vertax_2)
        adj_list[vertax_2].append(vertax_1)

    print(adj_list)
    dfs_list = deepcopy(adj_list)
    bfs_list = deepcopy(adj_list)

    for i in range(1, count + 1):
        dfs_list[i].sort()
    for i in range(1, count + 1):
        bfs_list[i].sort(reverse=True)

    for elem in dfs(start, dfs_list, count):
        print(elem, end=' ')
    print()
    for elem in bfs(start, bfs_list, count):
        print(elem, end=' ')
