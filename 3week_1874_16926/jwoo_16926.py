import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
	arr.append(list(map(int, sys.stdin.readline().split())))

def solution(arr, n, m, r):
	rotate = min(n, m) // 2
	rotate_line = [0 for _ in range(rotate)]
	new = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(rotate):
		rotate_line[i] = [0 for _ in range(2 * (n + m - 4 * i) - 4)]
	for i in range(len(rotate_line)):
		a, b = i, i
		for j in range(len(rotate_line[i])):
			rotate_line[i][j] = arr[a][b]
			new[a][b] = [i, j]
			if (b == i):
				if (a < n - 1 - i):
					a += 1
				else:
					b += 1
			elif (a == n - 1 - i):
				if (b < m - 1 - i):
					b += 1
				else:
					a -= 1
			elif (b == m - 1 - i):
				if (a > i):
					a -= 1
				else:
					b -= 1
			elif (a == i):
				if (b > i):
					b -= 1
	for i in range(n):
		for j in range(m):
			mod = len(rotate_line[new[i][j][0]])
			new[i][j] = rotate_line[new[i][j][0]][(new[i][j][1] - r) % mod]
	return new


answer = solution(arr, n, m, r)
for row in answer:
	for col in row:
		print(col, end=' ')
	print()