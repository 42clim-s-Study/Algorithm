import sys

n = int(input())
path = [[[0, 0]] for _ in range(n + 1)]
for _ in range(n - 1):
	parent, child, weight = map(int, sys.stdin.readline().split())
	path[child][0][0], path[child][0][1] = parent, weight
	path[parent].append([child, weight])

print(path)
stack = [[1, 0]]
visit = [0 for _ in range(n + 1)]
total_weight = 0
parent = []
while stack or parent:
	parent.append(stack.pop())
	if parent[-1][0] != 1:
		visit[parent[-1][0]] = 1
	total_weight += parent[-1][1]
	print(parent)
	if len(path[parent[-1][0]]) == 1:
		while visit[parent[-1][0]] == 1 and len(path[parent[-1][0]]) == 1:
			total_weight -= parent.pop()[1]
	else:
		while len(path[parent[-1][0]]) > 1:
			stack.append(path[parent[-1][0]].pop())
	print(parent)

