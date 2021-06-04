import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
storage = [0 for _ in range(n)]
index = []
empty = 0
for i in range(n):
	storage[i] = list(map(int, sys.stdin.readline().split()))
	for j in range(m):
		if storage[i][j] == 1:
			index.append([i, j])
		elif storage[i][j] == -1:
			empty += 1

que = deque(index)
day = 0
count = m * n - empty - len(index)
while que and count > 0:
	p = deque([])
	while que:
		p.append(que.popleft())
	for parent in p:
		child1 = [parent[0] - 1, parent[1]]
		child2 = [parent[0] + 1, parent[1]]
		child3 = [parent[0], parent[1] - 1]
		child4 = [parent[0], parent[1] + 1]
		if child1[0] >= 0 and storage[child1[0]][child1[1]] == 0:
			que.append(child1)
			storage[child1[0]][child1[1]] = 1
			count -= 1
		if child2[0] < n and storage[child2[0]][child2[1]] == 0:
			que.append(child2)
			storage[child2[0]][child2[1]] = 1
			count -= 1
		if child3[1] >= 0 and storage[child3[0]][child3[1]] == 0:
			que.append(child3)
			storage[child3[0]][child3[1]] = 1
			count -= 1
		if child4[1] < m and storage[child4[0]][child4[1]] == 0:
			que.append(child4)
			storage[child4[0]][child4[1]] = 1
			count -= 1
	day += 1

if count > 0:
	print(-1)
else:
	print(day)