import sys
from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	p1, p2 = map(int, sys.stdin.readline().split())
	tree[p1].append(p2)
	tree[p2].append(p1)

parent = [0 for _ in range(n + 1)]
parent[0], parent[1] = -1, -1
find_parent = n - 1

que = deque()
while tree[1]:
	p = tree[1].pop()
	que.append(p)
	parent[p] = 1
	find_parent -= 1

while find_parent > 0:
	p = que.popleft()
	while tree[p]:
		c = tree[p].pop()
		if parent[p] != 0 and parent[c] == 0:
			que.append(c)
			parent[c] = p
			find_parent -= 1

for i in range(2, n + 1):
	print(parent[i])