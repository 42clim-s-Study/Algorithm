import sys
from collections import deque

n = int(input())
computer = deque([[] for _ in range(n + 1)])
virus = [0 for _ in range(n + 1)]
connect = int(input())
for _ in range(connect):
	c1, c2 = map(int, sys.stdin.readline().split())
	computer[c1].append(c2)
	computer[c2].append(c1)

que = deque([1])
virus[1] = 1
while que:
	parent = que.popleft()
	while computer[parent]:
		que.append(computer[parent].pop())
		virus[que[-1]] += 1

count = 0
for i in range(2, n + 1):
	if virus[i] > 0:
		count += 1

print(count)