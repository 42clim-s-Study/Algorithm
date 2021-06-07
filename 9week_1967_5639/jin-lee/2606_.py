"""
2606번 바이러스
https://www.acmicpc.net/problem/2606

graph - adjacency list, adjacency matrix
dfs, bfs

예제 입력 1
7
6
1 2
2 3
1 5
5 2
5 6
4 7

예제 출력 1
4
"""


def dfs(start, list, count):
    stack = [start]
    visited = [0 for _ in range(count + 1)]
    while stack:
        curr = stack.pop()
        visited[curr] = 1
        while list[curr]:
            tmp = list[curr].pop()
            if not visited[tmp]:
                stack.append(tmp)
    ret = 0
    for i in visited:
        ret += i
    return ret


if __name__ == "__main__":
    count = int(input())
    connection = int(input())
    adj_list = [[] for _ in range(count + 1)]
    for _ in range(connection):
        vertax_1, vertax_2 = map(int, input().split())
        adj_list[vertax_1].append(vertax_2)
        adj_list[vertax_2].append(vertax_1)
    print(dfs(1, adj_list, count) - 1)
