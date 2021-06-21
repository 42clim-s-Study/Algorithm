import sys
from collections import deque

n = int(input())
house_map = [0 for _ in range(n)]
for i in range(n):
	house_map[i] = list(map(int, list(sys.stdin.readline().strip())))

def	is_in_range(child, n):
	if child[0] < 0 or child[1] < 0:
		return -1
	if child[0] >= n or child[1] >= n:
		return -1
	return 1

def	solution(house_map, n):
	visit = [[0 for _ in range(n)] for _ in range(n)]
	tool = [[1, 0], [-1, 0], [0, 1], [0, -1]]
	que = deque([])
	start = 0
	answer = [0 for _ in range(n * n + 1)]
	for i in range(n):
		for j in range(n):
			if house_map[i][j] == 1 and visit[i][j] == 0:
				start += 1
				visit[i][j] = start
				answer[start] += 1
				que.append([i, j])
				while que:
					parent = que.popleft()
					for factor in tool:
						child = [parent[i] + factor[i] for i in range(2)]
						if is_in_range(child, n) == 1 and house_map[child[0]][child[1]] == 1 and visit[child[0]][child[1]] == 0:
							que.append(child)
							visit[child[0]][child[1]] = start
							answer[start] += 1
	return answer[1:(start + 1)]

answer = solution(house_map, n)
answer.sort()
print(len(answer))
for factor in answer:
	print(factor)
