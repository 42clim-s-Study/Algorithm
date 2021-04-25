import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
cube = deque()
for i in range(n):
	cube.append(deque(map(int, sys.stdin.readline().split())))
	cube[i].appendleft(0)
cube.appendleft([0 for _ in range(m + 1)])

def	exterior_width(cube, n, m):
	row = 0
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if cube[i][j] > cube[i][j - 1]:
				row += cube[i][j] - cube[i][j - 1]
	col = 0
	for j in range(1, m + 1):
		for i in range(1, n + 1):
			if cube[i][j] > cube[i - 1][j]:
				col += cube[i][j] - cube[i - 1][j]
	width = row * 2 + col * 2 + n * m * 2
	return width

print(exterior_width(cube, n, m))
