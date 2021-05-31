import sys
import copy

# tree 리스트에 연결된 노드의 정보를 저장
n = int(input())
tree = [[[0, 0]] for _ in range(n + 1)]
for _ in range(n - 1):
	parent, child, weight = map(int, sys.stdin.readline().split())
	tree[child][0][0], tree[child][0][1] = parent, weight
	tree[parent].append([child, weight])

# 노드의 번호 == tree 리스트의 인덱스 번호
## 예를 들어 2번 노드와 연결된 노드의 정보를 알고 싶다면 tree[2]에 접근하면 된다

# tree[i]에는 i번 노드와 연결된 노드의 정보가 이중 리스트의 형태로 담긴다.
# tree[i][0]에는 tree[i]의 부모 노드 정보가, 그 이후(tree[i][0], tree[i][1], ...)에는 자식 노드 정보가 담긴다.
## tree[i] = [[tree[i]의 부모 노드 번호, weight0], [tree[i]의 1번째 노드 번호, weight1], [tree[i]의 2번째 노드 번호, weight2], ...]
# 1번은 루트 노드이므로, tree[1][0] = [0, 0]으로 초기화
# 0번 노드는 없으므로 tree[0] = [[0, 0]]으로 초기화



# path top에 있는 노드가 stack top에 있는 노드의 부모이면 1 반환
def is_parent(path_top, stack_top):
	global tree
	if path_top == tree[stack_top][0][0]:
		return 1
	return 0

# path 리스트에 추가하려는 노드(stack의 top에 있는 노드)가 이미 path 리스트에 존재하면 1 반환
def	is_in_path(path, stack_top):
	if len(path) == 0:
		return 0
	for factor in path:
		if stack and factor[0] == stack_top[0]:
			return 1
	return 0

# 부모인지 자식인지 따지지 않고, path top에 있는 노드와 stack top에 있는 노드가 연결되어 있으면 1 반환
def	is_connect(path, stack_top):
	global tree
	for factor in tree[stack_top]:
		if factor[0] == path[-1][0]:
			return 1
	return 0


# 루트 노드 (1번 노드) 부터 dfs, 가중치가 가장 높게 나온 경로의 마지막 노드를 찾늦다.
stack = [[1, 0]]
copy_tree = copy.deepcopy(tree)	# 방문한 노드를 pop() 해줄 것이므로 원본을 보존하기 위해 복사한 리스트 사용
total_weight = 0
last_node = []	# 가장 마지막 노드와 그 노드까지 가는 경로의 가중치를 저장할 리스트
path = []	# 지나온 노드를 저장해둘 리스트

while stack:
	path.append(stack.pop())
	total_weight += path[-1][1]
	if len(tree[path[-1][0]]) == 1:	# 더이상 자식이 없는 마지막 노드에 도달하면,
		last_node.append([total_weight, path[-1][0]])	# last_node 에 마지막 노드와 경로의 총 가중치를 저장
		## print(path, total_weight)
		total_weight -= path.pop()[1]
		# 스택의 탑에 있는 노드(다음번 path 리스트에 들어갈 노드)가 path 리스트 탑에 있는 노드의 자식이 아니면 계속 pop
		while path and stack and is_parent(path[-1][0], stack[-1][0]) == 0:
			total_weight -= path.pop()[1]
	else:
		# 노드의 자식이 남아있으면 모두 담아주기
		# len(...) > 1 로 설정하여 자식이 부모로 역행하는 것을 방지한다
		while len(copy_tree[path[-1][0]]) > 1:
			stack.append(copy_tree[path[-1][0]].pop())

last_node.sort()	# 가중치가 큰 것이 리스트의 마지막에 위치
max_weight = last_node[-1][0]
start_node = []		# 총 가중치가 동일한 경우가 있을 수 있으니, 리스트로 생성하여 max 값을 가진 경우를 전부 넣어주기
for factor in last_node:
	if factor[0] == max_weight:
		start_node.append(factor[1])


# 가중치가 가장 컸던 마지막 노드부터 다시 dfs
answer = 0
for start in start_node:
	stack = [[start, 0]]
	copy_tree = copy.deepcopy(tree)
	total_weight = 0
	path = []
	while stack:
		temp = stack.pop()
		if is_in_path(path, temp) == 0:		# path 리스트에 존재하지 않는 노드일 때만 append 하여 중복 방문 방지
			path.append(temp)
			total_weight += path[-1][1]
		if len(copy_tree[path[-1][0]]) == 0:	# 연결된 노드를 모두 한번씩 방문하고
			# 마지막으로 방문한 노드가 자식이 없는 마지막 노드일 때, answer 업데이트
			# path[-1][0] != start : start 노드도 자식이 없는 마지막 노드이기 때문에 예외 처리
			if path[-1][0] != start and len(tree[path[-1][0]]) == 1:
				answer = max(answer, total_weight)
				# print(path, total_weight)
			# 스택의 탑에 있는 노드(다음번 path 리스트에 들어갈 노드)가 path 리스트 탑에 있는 노드와 연결되어있지 않으면 아니면 계속 pop
			while path and stack and is_connect(path, stack[-1][0]) == 0:
				total_weight -= path.pop()[1]
		else:
			# 첫번째 dfs와 달리 자식에서 부모로 역행도 가능하기 때문에 len(...) > 0 로 설정
			while len(copy_tree[path[-1][0]]) > 0:
				stack.append(copy_tree[path[-1][0]].pop())

print(answer)





# sol00 : 메모리 초과

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