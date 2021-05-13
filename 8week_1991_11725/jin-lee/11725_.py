"""
11725 트리의 부모 찾기
https://www.acmicpc.net/problem/11725

간선을 나타내는 정점 두 개를 입력받고 루트를 1이라고 정했을 때,
각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
- 첫째 줄에 노드의 개수 N(2<=N<=100,000)이 주어진다.
- 둘때 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

입력 예1
7
1 6
6 3
3 5
4 1
2 4
4 7

출력 예1
4
6
1
3
1
4
"""


def dfs(tree, curr_node, parent):
    for i in tree[curr_node]:
        if parent[i] == 0:
            parent[i] = curr_node
            dfs(tree, i, parent)


if __name__ == "__main__":
    size = int(input())
    tree = [[] for _ in range(size + 1)]
    parent = [0 for _ in range(size + 1)]
    for _ in range(size - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    dfs(tree, curr_node=1, parent=parent)
    for i in range(2, size + 1):
        print(parent[i])

