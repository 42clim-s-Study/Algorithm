import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
storage = [[0 for _ in range(n)] for _ in range(h)]
ripe_index, empty = [], 0
for i in range(h):
	for j in range(n):
		storage[i][j] = list(map(int, sys.stdin.readline().split()))
		for k in range(m):
			if storage[i][j][k] == 1:
				ripe_index.append([i, j, k])
			elif storage[i][j][k] == -1:
				empty += 1

def	is_in_range(child, h, n, m):
	if child[0] < 0 or child[1] < 0 or child[2] < 0:
		return -1
	if child[0] >= h or child[1] >= n or child[2] >= m:
		return -1
	return 1

que = deque(ripe_index)
day = 0
unripe = m * n * h - empty - len(ripe_index)
adj_index = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
while que and unripe > 0:
	same_level = deque([])
	while que:
		same_level.append(que.popleft())
	for parent in same_level:
		for adj in adj_index:
			child = [parent[i] + adj[i] for i in range(3)]
			if is_in_range(child, h, n, m) == 1 and storage[child[0]][child[1]][child[2]] == 0:
				que.append(child)
				storage[child[0]][child[1]][child[2]] = 1
				unripe -= 1
	day += 1

if unripe > 0:
	print(-1)
else:
	print(day)