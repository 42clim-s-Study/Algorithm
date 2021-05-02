import sys
import copy

n = int(sys.stdin.readline().strip())
index = [[] for _ in range(n)]
matrix = [0 for _ in range(n)]
for i in range(n):
	matrix[i] = list(map(int, sys.stdin.readline().split()))
	for j in range(n):
		if matrix[i][j] == 1:
			index[i].append(j)

def	find_path(n, index, matrix):
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 1 or not index[i]:
				continue
			node = copy.deepcopy(index)
			next_path = []
			while node[i]:
				temp = node[i].pop()
				next_path.append(temp)
				matrix[i][temp] = 1
			while next_path and matrix[i][j] != 1:
				parent = next_path.pop()
				if parent == j:
					matrix[i][j] = 1
					break
				while node[parent]:
					temp = node[parent].pop()
					next_path.append(temp)
					matrix[parent][temp] = 1
	return matrix

answer = find_path(n, index, matrix)
for row in answer:
	for col in row:
		print(col, end=' ')
	print()