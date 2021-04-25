import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def josephus(n, k):
	que = deque(i for i in range(1, n + 1))
	remove = deque()
	while que:
		for _ in range(k - 1):
			que.append(que.popleft())
		remove.append(que.popleft())
	return remove

answer = josephus(n, k)
print('<', end= '')
for i in range(len(answer)):
	if i != len(answer) - 1:
		print(answer[i], end=', ')
	else:
		print(answer[i], end='')
print('>')