# import sys

# n = int(input())
# path = [[[0, 0]] for _ in range(n + 1)]
# for _ in range(n - 1):
# 	parent, child, weight = map(int, sys.stdin.readline().split())
# 	path[child][0][0], path[child][0][1] = parent, weight
# 	path[parent].append([child, weight])

# print(path)
# stack = [[1, 0]]
# visit = [0 for _ in range(n + 1)]
# total_weight = 0
# parent = []
# while stack or parent:
# 	parent.append(stack.pop())
# 	if parent[-1][0] != 1:
# 		visit[parent[-1][0]] = 1
# 	total_weight += parent[-1][1]
# 	print(parent)
# 	if len(path[parent[-1][0]]) == 1:
# 		while visit[parent[-1][0]] == 1 and len(path[parent[-1][0]]) == 1:
# 			total_weight -= parent.pop()[1]
# 	else:
# 		while len(path[parent[-1][0]]) > 1:
# 			stack.append(path[parent[-1][0]].pop())
# 	print(parent)




# 메모리 초과

import sys

n = int(input())
path = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n - 1):
	parent, child, weight = list(map(int, sys.stdin.readline().split()))
	path[parent - 1][child - 1] = weight
	path[child - 1][parent - 1] = weight

for start in range(n):
	for end in range(n):
		for mid in range(n):
			if start != end and path[start][mid] > 0 and path[mid][end] > 0:
				if path[start][end] == 0:
					path[start][end] = path[start][mid] + path[mid][end]
				else:
					path[start][end] = min(path[start][end], path[start][mid] + path[mid][end])

max_weight = 0
for i in range(n):
	temp = max(path[i])
	max_weight = max(max_weight, temp)
print(max_weight)