import sys
import copy

n = int(input())
tree = [[[0, 0]] for _ in range(n + 1)]
for _ in range(n - 1):
	parent, child, weight = map(int, sys.stdin.readline().split())
	tree[child][0][0], tree[child][0][1] = parent, weight
	tree[parent].append([child, weight])

# def is_parent(stack_top, path_top):
# 	global path
# 	# for i in range(1, len(path[path_top])):
# 	# 	child = path[path_top][i][0]
# 	# 	if stack_top == child:
# 	# 		return (1)
# 	if path_top == path[stack_top][0][0]:
# 	return (0)


stack = [[1, 0]]
copy_tree = copy.deepcopy(tree)
total_weight = 0
last_node = []
path = []
while stack:
	path.append(stack.pop())
	total_weight += path[-1][1]
	if len(tree[path[-1][0]]) == 1:
		last_node.append([total_weight, path[-1][0]])
		# print(path, total_weight)
		total_weight -= path.pop()[1]
		while path and stack and path[-1][0] != tree[stack[-1][0]][0][0]:
			total_weight -= path.pop()[1]
	else:
		while len(copy_tree[path[-1][0]]) > 1:
			stack.append(copy_tree[path[-1][0]].pop())

last_node.sort()
max_weight = last_node[-1][0]
start_node = []
for factor in last_node:
	if factor[0] == max_weight:
		start_node.append(factor[1])
# print(start_node)

def	is_in_path(path, stack_top):
	for factor in path:
		if stack and factor[0] == stack_top[0]:
			# print("hihi", path, stack)
			return 1
	# print("hihi", path, stack)
	return 0

def	is_connect(path, stack_top):
	global tree
	for factor in tree[stack_top]:
		if factor[0] == path[-1][0]:
			# print("hihi", path, stack)
			return 1
	# print("hihi", path, stack)
	return 0

stack = [[start_node[0], 0]]
copy_tree = copy.deepcopy(tree)
total_weight = 0
answer = 0
# last_node = []
visit = [0 for _ in range(n + 1)]
path = []
while stack:
	# print(path, stack)
	temp = stack.pop()
	if is_in_path(path, temp) == 0:
		path.append(temp)
		total_weight += path[-1][1]
	if len(copy_tree[path[-1][0]]) == 0:
		# last_node.append([total_weight, path[-1][0]])
		if len(tree[path[-1][0]]) == 1 and path[-1][0] != 0:
			answer = max(answer, total_weight)
			# print(path, total_weight)
		while path and stack and is_connect(path, stack[-1][0]) == 0:
			total_weight -= path.pop()[1]
	else:
		while len(copy_tree[path[-1][0]]) > 0:
			stack.append(copy_tree[path[-1][0]].pop())

print(answer)


# import sys

# n = int(input())
# path = [[0 for _ in range(n)] for _ in range(n)]
# for _ in range(n - 1):
# 	parent, child, weight = list(map(int, sys.stdin.readline().split()))
# 	path[parent - 1][child - 1] = weight
# 	path[child - 1][parent - 1] = weight

# for start in range(n):
# 	for end in range(n):
# 		for mid in range(n):
# 			if start != end and path[start][mid] > 0 and path[mid][end] > 0:
# 				if path[start][end] == 0:
# 					path[start][end] = path[start][mid] + path[mid][end]
# 				else:
# 					path[start][end] = min(path[start][end], path[start][mid] + path[mid][end])

# max_weight = 0
# for i in range(n):
# 	temp = max(path[i])
# 	max_weight = max(max_weight, temp)
# print(max_weight)