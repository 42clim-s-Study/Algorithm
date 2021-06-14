import sys
from collections import deque
import copy

n, m, v = map(int, sys.stdin.readline().split())
dfs = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, sys.stdin.readline().split())
	dfs[a].append(b)
	dfs[b].append(a)
bfs = copy.deepcopy(dfs)

stack = [v]
num = [i for i in range(n + 1)]
while stack:
	p = stack.pop()
	if num[p] != 0:
		print(p, end=' ')
	num[p] = 0
	while dfs[p]:
		x = dfs[p].pop(dfs[p].index(max(dfs[p])))
		if num[x] != 0:
			stack.append(x)

print()

stack = deque([v])
num = [i for i in range(n + 1)]
while stack:
	p = stack.popleft()
	if num[p] != 0:
		print(p, end=' ')
	num[p] = 0
	while bfs[p]:
		x = bfs[p].pop(bfs[p].index(min(bfs[p])))
		if num[x] != 0:
			stack.append(x)