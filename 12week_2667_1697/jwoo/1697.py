import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def solution(n, k):
	time = 0
	que = deque([n])
	visit = [0 for _ in range(100001)]
	while que:
		parent = deque([])
		while que:
			parent.append(que.popleft())
		for p in parent:
			if p == k:
				return time
			child = [p - 1, p + 1, p * 2]
			for c in child:
				if c >= 0 and c <= 100000 and visit[c] == 0:
					que.append(c)
					visit[c] = 1
		time += 1
	return time

print(solution(n, k))