import sys
from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
check = [[0 for _ in range(n)] for _ in range(n)]

que = deque([[r1, c1]])
flag = 0
move = 0
while que and not (r1 == r2 and c1 == c2):
	parent = deque()
	while que:
		parent.append(que.popleft())
	for p in parent:
		child1 = [p[0] - 2, p[1] - 1]
		child2 = [p[0] - 2, p[1] + 1]
		child3 = [p[0], p[1] - 2]
		child4 = [p[0], p[1] + 2]
		child5 = [p[0] + 2, p[1] - 1]
		child6 = [p[0] + 2, p[1] + 1]
		if child1[0] >= 0 and child1[1] >= 0 and check[child1[0]][child1[1]] != 1:
			que.append(child1)
			check[child1[0]][child1[1]] = 1
		if child2[0] >= 0 and child2[1] < n and check[child2[0]][child2[1]] != 1:
			que.append(child2)
			check[child2[0]][child2[1]] = 1
		if child3[1] >= 0 and check[child3[0]][child3[1]] != 1:
			que.append(child3)
			check[child3[0]][child3[1]] = 1
		if child4[1] < n and check[child4[0]][child4[1]] != 1:
			que.append(child4)
			check[child4[0]][child4[1]] = 1
		if child5[0] < n and child5[1] >= 0 and check[child5[0]][child5[1]] != 1:
			que.append(child5)
			check[child5[0]][child5[1]] = 1
		if child6[0] < n and child6[1] < n and check[child6[0]][child6[1]] != 1:
			que.append(child6)
			check[child6[0]][child6[1]] = 1
	move += 1
	if [r2, c2] in que:
		flag = 1
		break

if flag == 0:
	print(-1)
else:
	print(move)